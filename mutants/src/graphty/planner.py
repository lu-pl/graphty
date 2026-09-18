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

from graphty.utils.aggregation import Aggregation, Collect, Reduce
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁModelUnionDispatchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut: MutantDict = {}  # type: ignore


class ModelUnionDispatch:
    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁ__init____mutmut)
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
    def xǁModelUnionDispatchǁ__init____mutmut_orig(
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
    def xǁModelUnionDispatchǁ__init____mutmut_1(
        self,
        type_form: TypeForm,
        discriminator: str | Callable | None,
        planner: "LazyFramePlanner",
    ) -> None:
        self.type_form = None
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
    def xǁModelUnionDispatchǁ__init____mutmut_2(
        self,
        type_form: TypeForm,
        discriminator: str | Callable | None,
        planner: "LazyFramePlanner",
    ) -> None:
        self.type_form = type_form
        self.discriminator = None
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
    def xǁModelUnionDispatchǁ__init____mutmut_3(
        self,
        type_form: TypeForm,
        discriminator: str | Callable | None,
        planner: "LazyFramePlanner",
    ) -> None:
        self.type_form = type_form
        self.discriminator = discriminator
        self.planner = None

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
    def xǁModelUnionDispatchǁ__init____mutmut_4(
        self,
        type_form: TypeForm,
        discriminator: str | Callable | None,
        planner: "LazyFramePlanner",
    ) -> None:
        self.type_form = type_form
        self.discriminator = discriminator
        self.planner = planner

        self.model_members: list[type[BaseModel]] = None
        self.model_union_members: list[UnionType] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_5(
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
            for member in get_args(None)
            if is_pydantic_model_static_type(member)
        ]
        self.model_union_members: list[UnionType] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_6(
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
            for member in get_args(de_annotate(None))
            if is_pydantic_model_static_type(member)
        ]
        self.model_union_members: list[UnionType] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_7(
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
            if is_pydantic_model_static_type(None)
        ]
        self.model_union_members: list[UnionType] = [
            member
            for member in get_args(de_annotate(self.type_form))
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_8(
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
        self.model_union_members: list[UnionType] = None
    def xǁModelUnionDispatchǁ__init____mutmut_9(
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
            for member in get_args(None)
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_10(
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
            for member in get_args(de_annotate(None))
            if is_pydantic_model_union_static_type(member)
        ]
    def xǁModelUnionDispatchǁ__init____mutmut_11(
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
            if is_pydantic_model_union_static_type(None)
        ]

    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut)
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

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_orig(self) -> pl.Expr:
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

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_1(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=None)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_2(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = None
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_3(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = None

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_4(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            None,
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_5(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            None,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_6(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            None,
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_7(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_8(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_9(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(x),
            rest_whens,
            )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_10(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: None,
            rest_whens,
            when.otherwise(None),
        )

    def xǁModelUnionDispatchǁcompute_model_expr__mutmut_11(self) -> pl.Expr:
        match self.model_members, self.model_union_members:
            case [model], []:
                return self.planner._build_model_struct(model=model)

        whens = self._compute_whens()
        when, *rest_whens = whens

        return reduce(
            lambda x, y: y.otherwise(None),
            rest_whens,
            when.otherwise(None),
        )

    def _compute_whens(self) -> list["pl.When"]:
        return [
            *self._compute_model_whens(),
            *self._compute_model_union_whens(),
        ]

    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut)
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_orig(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_1(self) -> list["pl.When"]:
        if self.model_members:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_2(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = None

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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_3(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
            None,
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_4(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
            set.union,
            None,
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_5(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_6(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
            set.union,
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_7(self) -> list["pl.When"]:
        if not self.model_members:
            return []

        union_projection: set[str] = reduce(
            set.union,
            [
                self.planner.model_registry[member].model_projection
                for member in self.model_members
            ],
        )

        discriminator: Discriminator = None
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_8(self) -> list["pl.When"]:
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
        discriminator_value: str | Callable = None

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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_9(self) -> list["pl.When"]:
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

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_10(self) -> list["pl.When"]:
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

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_11(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_12(self) -> list["pl.When"]:
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
                discriminator_mapping: dict[tuple[str, ...], type[BaseModel]] = None

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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_13(self) -> list["pl.When"]:
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
                    get_args(None): model
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_14(self) -> list["pl.When"]:
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
                _model, *_ = None
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_15(self) -> list["pl.When"]:
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
                alias_map = None

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_16(self) -> list["pl.When"]:
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
                alias_map = AliasMap(model=None, projection=union_projection)

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_17(self) -> list["pl.When"]:
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
                alias_map = AliasMap(model=_model, projection=None)

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_18(self) -> list["pl.When"]:
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
                alias_map = AliasMap(projection=union_projection)

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_19(self) -> list["pl.When"]:
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
                alias_map = AliasMap(model=_model, )

                return [
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_20(self) -> list["pl.When"]:
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
                        None
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_21(self) -> list["pl.When"]:
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
                    pl.when(None).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_22(self) -> list["pl.When"]:
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
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(None)).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_23(self) -> list["pl.When"]:
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
                    pl.when(pl.col(None).is_in(list(k))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_24(self) -> list["pl.When"]:
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
                    pl.when(pl.col(alias_map[discriminator_value]).is_in(list(None))).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_25(self) -> list["pl.When"]:
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
                        pl.struct(None).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_26(self) -> list["pl.When"]:
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
                            *self.planner._generate_expressions(model=None)
                        )
                    )
                    for k, v in discriminator_mapping.items()
                ]

            case Callable():
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_27(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = None

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_28(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = None

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_29(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=None,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_30(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=None,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_31(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_32(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_33(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(None).map_elements(
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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_34(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        None
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_35(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(None).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_36(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression != k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_37(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(None).struct.with_fields(
                            *self.planner._generate_expressions(model=v)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_38(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

                discriminator_expression = pl.struct(union_projection).map_elements(
                    function=discriminator_value,
                    return_dtype=pl.String,
                )

                return [
                    pl.when(discriminator_expression == k).then(
                        pl.struct(union_projection).struct.with_fields(
                            *self.planner._generate_expressions(model=None)
                        )
                    )
                    for k, v in tag_mapping.items()
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_39(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(None)
                ]

            case _:  # pragma: no cover
                assert False, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_40(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert True, "Expected discriminator to be of type str | Callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_41(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "XXExpected discriminator to be of type str | Callable.XX"

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_42(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "expected discriminator to be of type str | callable."

    def xǁModelUnionDispatchǁ_compute_model_whens__mutmut_43(self) -> list["pl.When"]:
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
                tag_mapping: dict[str, TypeForm] = self._get_tag_mapping()

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
                    # model union members are handled in _compute_model_union_whens
                    if is_pydantic_model_static_type(v)
                ]

            case _:  # pragma: no cover
                assert False, "EXPECTED DISCRIMINATOR TO BE OF TYPE STR | CALLABLE."

    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut)
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

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_orig(self) -> list["pl.When"]:
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

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_1(self) -> list["pl.When"]:
        return list(
            None
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_2(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                None
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_3(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=None,
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_4(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, type_form),
                    discriminator=None,
                    planner=None,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_5(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_6(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, type_form),
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_7(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, type_form),
                    discriminator=None,
                    )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_8(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(None, type_form),
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_9(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, None),
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_10(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(type_form),
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    def xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_11(self) -> list["pl.When"]:
        return list(
            chain.from_iterable(
                ModelUnionDispatch(
                    type_form=cast(TypeForm, ),
                    discriminator=None,
                    planner=self.planner,
                )._compute_whens()
                for type_form in self.model_union_members
            )
        )

    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut)
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_orig(self) -> Discriminator:
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_1(self) -> Discriminator:
        if self.discriminator is None:
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_2(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=None)

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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_3(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = None

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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_4(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if (get_origin(self.type_form) is Annotated) and False else []
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_5(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if (get_origin(self.type_form) is Annotated) or True else []
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_6(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(None) if get_origin(self.type_form) is Annotated else []
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_7(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(None) is Annotated else []
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_8(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is not Annotated else []
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_9(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_10(self) -> Discriminator:
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

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_11(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:
                case FieldInfo(discriminator=discriminator):
                    assert discriminator is None, (
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

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_12(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:
                case FieldInfo(discriminator=discriminator):
                    assert discriminator is not None, (
                        "XXExpected discriminator to be non-None.XX"
                    )
                    return (
                        discriminator
                        if isinstance(discriminator, Discriminator)
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_13(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:
                case FieldInfo(discriminator=discriminator):
                    assert discriminator is not None, (
                        "expected discriminator to be non-none."
                    )
                    return (
                        discriminator
                        if isinstance(discriminator, Discriminator)
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_14(self) -> Discriminator:
        if self.discriminator is not None:
            return Discriminator(discriminator=self.discriminator)

        args = (
            get_args(self.type_form) if get_origin(self.type_form) is Annotated else []
        )

        for arg in args:
            match arg:
                case FieldInfo(discriminator=discriminator):
                    assert discriminator is not None, (
                        "EXPECTED DISCRIMINATOR TO BE NON-NONE."
                    )
                    return (
                        discriminator
                        if isinstance(discriminator, Discriminator)
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_15(self) -> Discriminator:
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
                        if (isinstance(discriminator, Discriminator)) and False
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_16(self) -> Discriminator:
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
                        if (isinstance(discriminator, Discriminator)) or True
                        else Discriminator(discriminator=discriminator)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_17(self) -> Discriminator:
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
                        else Discriminator(discriminator=None)
                    )

                case Discriminator():
                    return arg

        raise MissingDiscriminatorError(type_form=self.type_form)

    def xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_18(self) -> Discriminator:
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

        raise MissingDiscriminatorError(type_form=None)

    @_mutmut_mutated(mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut)
    def _get_tag_mapping(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_orig(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_1(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(None):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_2(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(None)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_3(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = None
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_4(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(None)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_5(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = None

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_6(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(None)

                yield tag.tag, model

        return dict(_generate())

    def xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_7(self) -> dict[str, TypeForm]:
        def _generate() -> Iterator[tuple[str, type[BaseModel]]]:
            for type_form in get_args(de_annotate(self.type_form)):
                model, *rest = get_args(type_form)
                tag = next(member for member in rest if isinstance(member, Tag))

                yield tag.tag, model

        return dict(None)

mutants_xǁModelUnionDispatchǁ__init____mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_8'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_9'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_10'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ__init____mutmut['xǁModelUnionDispatchǁ__init____mutmut_11'] = ModelUnionDispatch.xǁModelUnionDispatchǁ__init____mutmut_11 # type: ignore # mutmut generated

mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_8'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_9'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_10'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁcompute_model_expr__mutmut['xǁModelUnionDispatchǁcompute_model_expr__mutmut_11'] = ModelUnionDispatch.xǁModelUnionDispatchǁcompute_model_expr__mutmut_11 # type: ignore # mutmut generated

mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_8'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_9'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_10'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_11'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_11 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_12'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_12 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_13'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_13 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_14'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_14 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_15'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_15 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_16'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_16 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_17'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_17 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_18'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_18 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_19'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_19 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_20'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_20 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_21'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_21 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_22'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_22 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_23'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_23 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_24'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_24 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_25'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_25 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_26'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_26 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_27'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_27 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_28'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_28 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_29'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_29 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_30'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_30 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_31'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_31 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_32'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_32 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_33'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_33 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_34'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_34 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_35'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_35 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_36'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_36 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_37'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_37 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_38'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_38 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_39'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_39 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_40'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_40 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_41'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_41 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_42'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_42 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_whens__mutmut_43'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_whens__mutmut_43 # type: ignore # mutmut generated

mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_8'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_9'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_10'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut['xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_11'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_compute_model_union_whens__mutmut_11 # type: ignore # mutmut generated

mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_8'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_9'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_10'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_11'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_11 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_12'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_12 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_13'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_13 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_14'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_14 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_15'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_15 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_16'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_16 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_17'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_17 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_resolve_discriminator__mutmut['xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_18'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_resolve_discriminator__mutmut_18 # type: ignore # mutmut generated

mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['_mutmut_orig'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_1'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_2'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_3'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_4'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_5'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_6'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelUnionDispatchǁ_get_tag_mapping__mutmut['xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_7'] = ModelUnionDispatch.xǁModelUnionDispatchǁ_get_tag_mapping__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLazyFramePlannerǁrun__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut: MutantDict = {}  # type: ignore


class LazyFramePlanner[TModel: type[BaseModel]]:
    @_mutmut_mutated(mutants_xǁLazyFramePlannerǁ__init____mutmut)
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
    def xǁLazyFramePlannerǁ__init____mutmut_orig(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_1(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = None
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_2(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = None

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_3(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if (isinstance(data, pl.LazyFrame)) and False else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_4(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if (isinstance(data, pl.LazyFrame)) or True else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_5(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=None)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=self._base_cols)
        )
    def xǁLazyFramePlannerǁ__init____mutmut_6(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = None
    def xǁLazyFramePlannerǁ__init____mutmut_7(
        self, model: TModel, data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.lazy_frame: pl.LazyFrame = (
            data if isinstance(data, pl.LazyFrame) else pl.LazyFrame(data=data)
        )

        self.model_registry: MutableMapping[type[BaseModel], ModelInfo] = (
            ModelInfoRegistry(base_cols=None)
        )

    @_mutmut_mutated(mutants_xǁLazyFramePlannerǁrun__mutmut)
    def run(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_orig(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_1(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = None
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_2(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = None
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_3(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = None

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_4(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is not None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_5(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(None)
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_6(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=None)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_7(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(None))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_8(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(None, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_9(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=None).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_10(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_11(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, ).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_12(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=False).agg(
            *self._generate_expressions(model=self.model, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_13(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=None, group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_14(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=None),
        )

    def xǁLazyFramePlannerǁrun__mutmut_15(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(group_context=True),
        )

    def xǁLazyFramePlannerǁrun__mutmut_16(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, ),
        )

    def xǁLazyFramePlannerǁrun__mutmut_17(self) -> pl.LazyFrame:
        model_info: ModelInfo[TModel] = self.model_registry[self.model]
        group_by: str | None = model_info.group_by
        model_projection: set[str] = model_info.model_projection

        if group_by is None:
            if self.model.model_fields:
                return self.lazy_frame.with_columns(
                    *self._generate_expressions(model=self.model)
                ).drop(self._base_cols.difference(model_projection))
            return self.lazy_frame

        return self.lazy_frame.group_by(group_by, maintain_order=True).agg(
            *self._generate_expressions(model=self.model, group_context=False),
        )

    @cached_property
    def _base_cols(self) -> set[str]:
        return set(self.lazy_frame.collect_schema().names())

    @_mutmut_mutated(mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut)
    def _generate_expressions(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_orig(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_1(
        self, model: type[BaseModel], group_context: bool = True
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_2(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = None
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_3(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(None, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_4(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, None)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_5(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_6(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, )
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_7(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = None

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_8(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=None, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_9(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=None
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_10(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_11(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_12(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(None):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_13(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = None
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_14(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    None
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_15(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=None).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_16(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = None
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_17(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation and Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_18(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if (not group_context) and False else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_19(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if (not group_context) or True else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_20(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_21(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(None)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_22(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(None):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_23(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = None
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_24(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(None)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_25(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=None,
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_26(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=None,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_27(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=None,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_28(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_29(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_30(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_31(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(None, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_32(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, None),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_33(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_34(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, ),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_35(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(None)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_36(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = None
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_37(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation and Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_38(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if (not group_context) and False else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_39(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if (not group_context) or True else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_40(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_41(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(None)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_42(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(None):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_43(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = None

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_44(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(None)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_45(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(None):
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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_46(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = None
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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_47(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(None)
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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_48(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=None
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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_49(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(None):
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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_50(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = None
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_51(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                        .alias(None)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_52(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=None,
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_53(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(TypeForm, item_annotation),
                            discriminator=None,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_54(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                            planner=None,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_55(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_56(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(TypeForm, item_annotation),
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_57(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                            )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_58(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(None, item_annotation),
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_59(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(TypeForm, None),
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_60(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(item_annotation),
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_61(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

                if is_pydantic_model_static_type(item_annotation):
                    inner: pl.Expr = self._build_model_struct(
                        model=item_annotation
                    ).alias(field_name)
                elif is_pydantic_model_union_static_type(item_annotation):
                    inner = (
                        ModelUnionDispatch(
                            # item_annotation is the full TypeForm required for union resolution
                            type_form=cast(TypeForm, ),
                            discriminator=field_info.discriminator,
                            planner=self,
                        )
                        .compute_model_expr()
                        .alias(field_name)
                    )
                else:
                    alias_map = self.model_registry[model].alias_map
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_62(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                    alias_map = None
                    inner: pl.Expr = pl.col(alias_map[field_name])

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_63(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                    inner: pl.Expr = None

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_64(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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
                    inner: pl.Expr = pl.col(None)

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_65(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = None
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_66(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation and Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_67(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = None

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_68(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(None)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_69(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = None
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_70(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is not None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_71(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=None)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_72(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if (group_context) and False
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_73(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if (group_context) or True
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_74(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=None)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_75(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = None

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_76(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_77(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = None

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_78(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col == group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_79(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = None
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_80(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation and Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_81(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = None
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_82(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(None)
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_83(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(None))
                        yield expr if group_context else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_84(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if (group_context) and False else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_85(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if (group_context) or True else expr.over(group_by)

    def xǁLazyFramePlannerǁ_generate_expressions__mutmut_86(
        self, model: type[BaseModel], group_context: bool = False
    ) -> Iterator[pl.Expr]:
        for field_name, field_info in model.model_fields.items():
            annotation = cast(TypeForm, field_info.annotation)
            aggregation: Aggregation | None = get_metadata(
                field_info=field_info, cls=Aggregation
            )

            if is_pydantic_model_static_type(annotation):
                expr: pl.Expr = self._build_model_struct(model=annotation).alias(
                    field_name
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_pydantic_model_union_static_type(annotation):
                expr: pl.Expr = (
                    ModelUnionDispatch(
                        # pass full TypeForm for discriminator resolution
                        type_form=cast(TypeForm, get_annotations(model)[field_name]),
                        discriminator=field_info.discriminator,
                        planner=self,
                    )
                    .compute_model_expr()
                    .alias(field_name)
                )
                reduction: Aggregation = aggregation or Reduce()
                yield expr if not group_context else reduction(expr)

            elif is_parametrized_list_static_type(annotation):
                item_annotation, *_ = get_args(annotation)

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

                agg: Aggregation = aggregation or Collect()
                expr: pl.Expr = agg(inner)

                partition_value = self.model_registry[model].group_by
                if partition_value is None:
                    raise MissingGroupByError(model=model)

                yield (
                    expr
                    if group_context
                    else expr.implode().over(partition_by=partition_value)
                )

            else:
                group_by: str | None = self.model_registry[model].group_by

                if group_by is not None:
                    col = self.model_registry[model].alias_map[field_name]

                    if col != group_by:
                        reduction: Aggregation = aggregation or Reduce()
                        expr: pl.Expr = reduction(pl.col(col))
                        yield expr if group_context else expr.over(None)

    @_mutmut_mutated(mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut)
    def _build_model_struct(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_orig(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_1(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = None
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_2(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = None

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_3(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = None
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_4(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if (group_by is None) and False
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_5(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if (group_by is None) or True
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_6(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(None) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_7(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is not None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_8(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(None)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_9(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = None
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_10(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=None, group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_11(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=None),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_12(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(group_context=False),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_13(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, ),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_14(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=True),
        ]
        return pl.struct(exprs or self._base_cols)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_15(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(None)

    def xǁLazyFramePlannerǁ_build_model_struct__mutmut_16(self, model: type[BaseModel]) -> pl.Expr:
        model_info: ModelInfo = self.model_registry[model]
        group_by = model_info.group_by

        col_exprs: list[pl.Expr] = (
            [pl.col(member) for member in model_info.model_projection]
            if group_by is None
            else [pl.col(group_by)]
        )
        exprs: list[pl.Expr] = [
            *col_exprs,
            *self._generate_expressions(model=model, group_context=False),
        ]
        return pl.struct(exprs and self._base_cols)

mutants_xǁLazyFramePlannerǁ__init____mutmut['_mutmut_orig'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_1'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_2'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_3'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_4'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_5'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_6'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ__init____mutmut['xǁLazyFramePlannerǁ__init____mutmut_7'] = LazyFramePlanner.xǁLazyFramePlannerǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁLazyFramePlannerǁrun__mutmut['_mutmut_orig'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_1'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_2'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_3'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_4'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_5'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_6'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_7'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_8'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_9'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_10'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_11'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_12'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_13'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_14'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_15'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_16'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁrun__mutmut['xǁLazyFramePlannerǁrun__mutmut_17'] = LazyFramePlanner.xǁLazyFramePlannerǁrun__mutmut_17 # type: ignore # mutmut generated

mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['_mutmut_orig'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_1'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_2'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_3'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_4'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_5'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_6'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_7'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_8'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_9'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_10'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_11'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_12'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_13'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_14'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_15'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_16'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_17'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_18'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_19'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_20'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_21'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_22'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_23'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_24'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_25'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_26'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_27'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_28'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_29'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_30'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_30 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_31'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_31 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_32'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_32 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_33'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_33 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_34'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_34 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_35'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_35 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_36'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_36 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_37'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_37 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_38'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_38 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_39'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_39 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_40'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_40 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_41'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_41 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_42'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_42 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_43'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_43 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_44'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_44 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_45'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_45 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_46'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_46 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_47'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_47 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_48'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_48 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_49'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_49 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_50'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_50 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_51'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_51 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_52'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_52 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_53'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_53 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_54'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_54 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_55'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_55 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_56'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_56 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_57'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_57 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_58'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_58 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_59'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_59 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_60'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_60 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_61'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_61 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_62'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_62 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_63'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_63 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_64'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_64 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_65'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_65 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_66'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_66 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_67'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_67 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_68'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_68 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_69'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_69 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_70'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_70 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_71'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_71 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_72'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_72 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_73'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_73 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_74'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_74 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_75'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_75 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_76'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_76 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_77'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_77 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_78'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_78 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_79'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_79 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_80'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_80 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_81'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_81 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_82'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_82 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_83'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_83 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_84'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_84 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_85'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_85 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_generate_expressions__mutmut['xǁLazyFramePlannerǁ_generate_expressions__mutmut_86'] = LazyFramePlanner.xǁLazyFramePlannerǁ_generate_expressions__mutmut_86 # type: ignore # mutmut generated

mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['_mutmut_orig'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_1'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_2'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_3'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_4'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_5'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_6'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_7'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_8'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_9'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_10'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_11'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_12'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_13'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_14'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_15'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLazyFramePlannerǁ_build_model_struct__mutmut['xǁLazyFramePlannerǁ_build_model_struct__mutmut_16'] = LazyFramePlanner.xǁLazyFramePlannerǁ_build_model_struct__mutmut_16 # type: ignore # mutmut generated
