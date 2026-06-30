from collections.abc import Callable, Iterable, Iterator
from functools import cached_property, reduce
from itertools import chain
from types import UnionType
from typing import Annotated, Literal, cast, get_args, get_origin, overload

import polars as pl
from pydantic import BaseModel, Discriminator, Tag
from pydantic.fields import FieldInfo
from typing_extensions import TypeForm, get_annotations

from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import MissingDiscriminatorError, MissingGroupByError
from graphty.utils.type_utils import (
    de_annotate,
    is_parametrized_list_static_type,
    is_pydantic_model_static_type,
    is_pydantic_model_union_static_type,
    is_structured_field_static_type,
)
from graphty.utils.types import Agg


def get_model_projection(model: type[BaseModel], base_cols: set[str]) -> set[str]:
    alias_map = AliasMap(model=model, projection=base_cols)

    return {
        alias_map[field_name]
        for field_name, field_info in model.model_fields.items()
        if not is_structured_field_static_type(field_info.annotation)
    }


def build_model_struct(model: type[BaseModel], base_cols: set[str]) -> pl.Struct:
    model_projection: set[str] = get_model_projection(model=model, base_cols=base_cols)
    exprs: chain[pl.Expr] = chain(
        [pl.col(member) for member in model_projection],
        Exprs(model=model, base_cols=base_cols),
    )

    return pl.struct(*exprs)


@overload
def get_group_by_value(
    model: type[BaseModel], base_cols: set[str], strict: Literal[True] = True
) -> str: ...


@overload
def get_group_by_value(
    model: type[BaseModel], base_cols: set[str], strict: Literal[False]
) -> str | None: ...


def get_group_by_value(
    model: type[BaseModel], base_cols: set[str], strict: bool = True
) -> str | None:
    try:
        group_by_value = model.model_config["group_by"]
    except KeyError:
        if strict:
            raise MissingGroupByError(model=model)
        return None
    else:
        alias_map = AliasMap(model=model, projection=base_cols)
        return alias_map[group_by_value]


class ModelUnionDispatch:
    def __init__(
        self,
        type_form: TypeForm,
        base_cols: set[str],
        discriminator: str | Callable | None,
    ) -> None:
        self.type_form = type_form
        self.base_cols = base_cols
        self.discriminator = discriminator

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
                return build_model_struct(model=model, base_cols=self.base_cols)

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
                get_model_projection(model=member, base_cols=self.base_cols)
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
                            *Exprs(model=v, base_cols=self.base_cols),
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
                            *Exprs(model=v, base_cols=self.base_cols),
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
                    base_cols=self.base_cols,
                    discriminator=None,
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

    # TODO: this needs to be more defensive and raise a clear exception in case Tags cannot be retrieved
    def _get_tag_mapping(self):
        """Prototype; this needs proper abstraction."""

        def _generate():
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())


class Exprs(Iterable[pl.Expr]):
    def __init__(
        self, model: type[BaseModel], base_cols: set[str], group_context: bool = False
    ) -> None:
        self.model = model
        self.base_cols = base_cols
        self.group_context = group_context

    def __iter__(self) -> Iterator[pl.Expr]:
        for field_name, field_info in self.model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = build_model_struct(
                    model=annotation, base_cols=self.base_cols
                ).alias(field_name)

                yield (expr.first() if self.group_context else expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        type_form=get_annotations(self.model)[
                            field_name
                        ],  # pass full TypeForm for discriminator resolution
                        base_cols=self.base_cols,
                        discriminator=field_info.discriminator,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                yield (expr.first() if self.group_context else expr)

            elif is_parametrized_list_static_type(annotation):
                (item_annotation,) = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = build_model_struct(
                        model=item_annotation, base_cols=self.base_cols
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            type_form=item_annotation,  # pyright: ignore
                            base_cols=self.base_cols,
                            discriminator=field_info.discriminator,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = AliasMap(model=self.model, projection=self.base_cols)
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Agg = self._get_agg(field_info)
                expr: pl.Expr = agg.apply_to(inner)

                partition_value: str = get_group_by_value(
                    model=self.model, base_cols=self.base_cols
                )

                yield (
                    expr
                    if self.group_context
                    else expr.implode().over(partition_by=partition_value)
                )

    @staticmethod
    def _get_agg(field_info: FieldInfo) -> Agg:
        agg: Agg | None = next(
            (entry for entry in field_info.metadata if isinstance(entry, Agg)), None
        )
        return agg or Agg()


class LazyFramePlanner:
    def __init__(
        self, model: type[BaseModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

    def run(self) -> pl.LazyFrame:
        group_by: str | None = get_group_by_value(
            model=self.model, base_cols=self._base_cols, strict=False
        )
        model_projection: set[str] = get_model_projection(
            model=self.model, base_cols=self._base_cols
        )

        if group_by is None:
            return self.lazy_frame.with_columns(
                *Exprs(model=self.model, base_cols=self._base_cols)
            ).drop(self._base_cols.difference(model_projection))

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *[pl.col(col).first() for col in model_projection.difference({group_by})],
            *Exprs(model=self.model, base_cols=self._base_cols, group_context=True),
        )

    @cached_property
    def _base_cols(self) -> set[str]:
        return set(self.lazy_frame.collect_schema().names())
