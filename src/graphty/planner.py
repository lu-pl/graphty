from collections.abc import Callable, Iterator
from functools import cached_property, reduce
from itertools import chain
from types import UnionType
from typing import (
    Annotated,
    MutableMapping,
    cast,
    get_args,
    get_origin,
)

import polars as pl
from pydantic import BaseModel, Discriminator, Tag
from pydantic.fields import FieldInfo
from typing_extensions import TypeForm, get_annotations

from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import (
    MissingDiscriminatorError,
    MissingGroupByError,
)
from graphty.utils.model_info import ModelInfo, ModelInfoRegistry
from graphty.utils.type_utils import (
    de_annotate,
    get_metadata,
    is_parametrized_list_static_type,
    is_pydantic_model_static_type,
    is_pydantic_model_union_static_type,
)
from graphty.utils.types import Agg


class ModelUnionDispatch:
    def __init__(
        self,
        type_form: TypeForm,
        discriminator: str | Callable | None,
        planner: "LazyFramePlanner",
    ) -> None:
        self.type_form = type_form
        self.discriminator = discriminator
        self.planner = planner

        self.model_members: list[type[BaseModel]] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_static_type(member)
        ]
        self.model_union_members: list[UnionType] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_union_static_type(member)
        ]

    def compute_model_expr(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            when.otherwise(None),
        )

    def _compute_whens(self) -> list["pl.When"]:
        return [
            *self._compute_model_whens(),
            *self._compute_model_union_whens(),
        ]

    def _compute_model_whens(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
            set.union,
            [
                self.planner.model_registry[member].model_projection
                for member in self.model_members
            ],
        )

        discriminator: Discriminator = self._resolve_discriminator()
        discriminator_value: str | Callable = discriminator.discriminator

        match discriminator_value:
            case str():
                discriminator_mapping: dict[tuple[str, ...], type[BaseModel]] = {
                    get_args(model.model_fields[discriminator_value].annotation): model
                    for model in self.model_members
                }

                # Resolve the discriminator field name to its column alias.
                # Pydantic requires all union members to share the same alias for the discriminator field,
                # so the first (or any) union member is sufficient for instantiating AliasMap.
                _model, *_ = self.model_members
                alias_map = AliasMap(model=_model, projection=union_projection)

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, type[BaseModel]] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def _compute_model_union_whens(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, type_form),
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def _resolve_discriminator(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:
                case FieldInfo(discriminator=discriminator):
                    assert discriminator is not None, (
                        "Expected discriminator to be non-None."
                    )
                    return (
                        discriminator
                        if isinstance(discriminator, Discriminator)
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def _get_tag_mapping(self) -> dict[str, type[BaseModel]]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())


class LazyFramePlanner[TModel: type[BaseModel]]:
    def __init__(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )

    def run(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                # TODO: when Opacity/planner disengagement is implemented, fields marked
                # as Opaque should not count as "model fields" for this check — a model
                # with only Opaque fields should also return the raw frame.
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *[pl.col(col).first() for col in model_projection.difference({group_by})],
            *self._generate_expressions(model=self.model, group_context=True),
        )

    @cached_property
    def _base_cols(self) -> set[str]:
        return set(self.lazy_frame.collect_schema().names())

    def _generate_expressions(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )

                yield (expr.first() if group_context else expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=get_annotations(model)[field_name],
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                yield (expr.first() if group_context else expr)

            elif is_parametrized_list_static_type(annotation):
                (item_annotation,) = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(TypeForm, item_annotation),
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Agg = get_metadata(field_info=field_info, cls=Agg) or Agg()
                expr: pl.Expr = agg.apply_to(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

    def _build_model_struct(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        exprs: list[pl.Expr] = [
            *[pl.col(member) for member in model_info.model_projection],
            *self._generate_expressions(model=model),
        ]

        return pl.struct(exprs or self._base_cols)
