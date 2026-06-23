from collections.abc import Callable, Iterable, Iterator
from functools import cached_property, reduce
from itertools import chain
from types import UnionType
from typing import Annotated, cast, get_args, get_origin

import polars as pl
from pydantic import BaseModel, Discriminator, Tag
from pydantic.fields import FieldInfo
from typing_extensions import TypeForm, get_annotations

from graphty.utils import alias_map
from graphty.utils.alias_map import AliasMap
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
                # TODO: this duplicates Exprs._struct_expr and should be abstracted
                model_projection: set[str] = get_model_projection(
                    model=model, base_cols=self.base_cols
                )
                return pl.struct(model_projection).struct.with_fields(
                    *Exprs(model=model, base_cols=self.base_cols),
                )

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

                return [
                    pl.when(pl.col(discriminator_value).is_in(list(k))).then(
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

            case _:
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

        msg = (
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for type form '{self.type_form}'."
        )
        raise ValueError(msg)

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

        self.model_projection: set[str] = get_model_projection(
            model=model, base_cols=self.base_cols
        )
        self.alias_map = AliasMap(model=model, projection=self.model_projection)

    def __iter__(self) -> Iterator[pl.Expr]:
        for field_name, field_info in self.model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._struct_expr(model=annotation).alias(field_name)
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

                partition_value: str = self._get_partition_value(model=self.model)
                agg: Agg = self._get_agg(field_info)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._struct_expr(model=item_annotation).alias(
                        field_name
                    )
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
                    inner: pl.Expr = pl.col(self.alias_map[field_name])

                expr: pl.Expr = agg.apply_to(inner)
                yield (
                    expr
                    if self.group_context
                    else expr.implode().over(partition_by=partition_value)
                )

    def _struct_expr(self, model: type[BaseModel]) -> pl.Expr:
        exprs: chain[pl.Expr] = chain(
            [pl.col(member) for member in self.model_projection],
            Exprs(model=model, base_cols=self.base_cols),
        )
        return pl.struct(*exprs)

    @staticmethod
    def _get_partition_value(model: type[BaseModel]) -> str:
        try:
            partition_value = model.model_config["group_by"]  # type: ignore
        except KeyError:
            raise Exception(
                f"Model '{model.__name__}' with aggregation target "
                "does not specify ConfigDict.group_by."
            )
        else:
            return partition_value

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
        alias_map = AliasMap(model=self.model, projection=self._base_cols)
        group_by: str | None = alias_map[self.model.model_config.get("group_by")]

        model_projection: set[str] = get_model_projection(
            model=self.model, base_cols=self._base_cols
        )

        if group_by is None:
            return self.lazy_frame.with_columns(
                *Exprs(model=self.model, base_cols=self._base_cols)
            ).drop(self._base_cols.difference(model_projection))

        return (
            self.lazy_frame.group_by(group_by, maintain_order=True)
            .agg(
                *[
                    pl.col(col).first()
                    for col in model_projection.difference({group_by})
                ],
                *Exprs(model=self.model, base_cols=self._base_cols, group_context=True),
            )
            .drop(group_by if group_by not in model_projection else [])
        )

    @cached_property
    def _base_cols(self) -> set[str]:
        return set(self.lazy_frame.collect_schema().names())
