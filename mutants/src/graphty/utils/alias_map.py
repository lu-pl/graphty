from collections import UserDict
from collections.abc import Callable, Iterator

from graphty.utils.exceptions import AliasResolutionError
from pydantic import AliasChoices, BaseModel
from pydantic.fields import FieldInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAliasMapǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAliasMapǁ_generate_alias_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAliasMapǁ_compute_alias_candidates__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAliasMapǁ_resolve_alias__mutmut: MutantDict = {}  # type: ignore


class AliasMap(UserDict):
    """Custom mapping for resolving Pydantic field validation aliases.

    E.g. for a given model

    class Point(BaseModel):
        a: int = Field(alias="x")
        y: int

    the mapping would compute to {"a": "x", "y": y}.

    Alias choices, alias generators and alias priority are supported;
    alias choices are resolved against a projection.

    Note that AliasPath is currently not supported.
    """

    @_mutmut_mutated(mutants_xǁAliasMapǁ__init____mutmut)
    def __init__(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if projection is None else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_orig(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if projection is None else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_1(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = None
        self.projection: set[str] = set() if projection is None else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_2(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = None

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_3(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if (projection is None) and False else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_4(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if (projection is None) or True else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_5(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if projection is not None else projection

        self.data = dict(self._generate_alias_map())

    def xǁAliasMapǁ__init____mutmut_6(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if projection is None else projection

        self.data = None

    def xǁAliasMapǁ__init____mutmut_7(
        self, model: type[BaseModel], projection: set[str] | None = None
    ) -> None:
        self.model = model
        self.projection: set[str] = set() if projection is None else projection

        self.data = dict(None)

    @_mutmut_mutated(mutants_xǁAliasMapǁ_generate_alias_map__mutmut)
    def _generate_alias_map(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_orig(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_1(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = None

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_2(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = None

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_3(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(None, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_4(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, None)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_5(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_6(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, )

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_7(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_8(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_9(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_10(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)

    def xǁAliasMapǁ_generate_alias_map__mutmut_11(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = None

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_12(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        None, None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_13(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_14(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_15(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i not in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_16(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is not None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_17(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=None,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_18(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=None,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_19(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=None,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_20(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=None,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_21(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_22(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_23(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_24(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_25(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert True, "This should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_26(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "XXThis should never happen.XX"

    def xǁAliasMapǁ_generate_alias_map__mutmut_27(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "this should never happen."

    def xǁAliasMapǁ_generate_alias_map__mutmut_28(self) -> Iterator[tuple[str, str]]:
        """Generate an alias mapping.

        For every field in a given model, the generator resolves aliases
        and yields 2-tuples representing key/value pairs.
        """

        alias_resolver: Callable[[str, FieldInfo], list[str]] = (
            self._get_alias_resolver()
        )

        for k, v in self.model.model_fields.items():
            aliases: list[str] = alias_resolver(k, v)

            match aliases:
                case []:
                    yield k, k
                case [alias]:
                    yield (k, alias)
                case [_alias, *_aliases] as aliases:
                    alias: str | None = next(
                        (i for i in aliases if i in self.projection), None
                    )

                    if alias is None:
                        raise AliasResolutionError(
                            field_name=k,
                            model=self.model,
                            aliases=aliases,
                            projection=self.projection,
                        )

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "THIS SHOULD NEVER HAPPEN."

    @_mutmut_mutated(mutants_xǁAliasMapǁ_get_alias_resolver__mutmut)
    def _get_alias_resolver(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_orig(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_1(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = None

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_2(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get(None) is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_3(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("XXpopulate_by_nameXX") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_4(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("POPULATE_BY_NAME") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_5(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_6(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = None
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_7(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "XXConfig option 'populate_by_name' is not supported. XX"
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_8(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_9(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "CONFIG OPTION 'POPULATE_BY_NAME' IS NOT SUPPORTED. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_10(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "XXUse Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead.XX"
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_11(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "use pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_12(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "USE PYDANTIC >=2.11 FLAGS 'VALIDATE_BY_NAME'/'VALIDATE_BY_ALIAS' INSTEAD."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_13(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(None)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_14(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = None

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_15(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get(None, False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_16(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", None),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_17(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get(False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_18(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", ),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_19(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("XXvalidate_by_nameXX", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_20(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("VALIDATE_BY_NAME", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_21(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", True),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_22(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get(None, True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_23(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", None),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_24(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get(True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_25(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", ),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_26(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("XXvalidate_by_aliasXX", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_27(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("VALIDATE_BY_ALIAS", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_28(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", False),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_29(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_30(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_31(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_32(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_33(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)

    def xǁAliasMapǁ_get_alias_resolver__mutmut_34(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case False, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_35(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, True:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_36(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: None
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_37(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case True, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_38(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, False:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_39(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: None
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_40(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=None
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_41(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case False, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_42(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, False:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_43(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: None
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_44(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=None),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_45(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                True,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_46(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                True,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_47(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = None
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_48(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "XXInvalid config: validate_by_name=False, validate_by_alias=False.XX"
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_49(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "invalid config: validate_by_name=false, validate_by_alias=false."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_50(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "INVALID CONFIG: VALIDATE_BY_NAME=FALSE, VALIDATE_BY_ALIAS=FALSE."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_51(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(None)
            case _:  # pragma: no cover
                assert False, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_52(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert True, "This should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_53(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "XXThis should never happen.XX"

    def xǁAliasMapǁ_get_alias_resolver__mutmut_54(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "this should never happen."

    def xǁAliasMapǁ_get_alias_resolver__mutmut_55(self) -> Callable[[str, FieldInfo], list[str]]:
        """Helper for acquiring an alias resolver.

        An alias resolver computes alias candidates given a field name and
        FieldInfo object and according to validate_by_name/validate_by_alias flags.

        Note that the deprecated populate_by_name flag is not supported.
        """

        model_config = self.model.model_config

        if model_config.get("populate_by_name") is not None:
            msg = (
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            )
            raise ValueError(msg)

        validate_by_name, validate_by_alias = (
            model_config.get("validate_by_name", False),
            model_config.get("validate_by_alias", True),
        )

        match validate_by_name, validate_by_alias:
            case True, False:
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:
                return lambda field_name, field_info: [
                    field_name,
                    *self._compute_alias_candidates(field_info=field_info),
                ]
            case (
                False,
                False,
            ):  # pragma: no cover; False, False raises error in Pydantic
                msg = "Invalid config: validate_by_name=False, validate_by_alias=False."
                raise ValueError(msg)
            case _:  # pragma: no cover
                assert False, "THIS SHOULD NEVER HAPPEN."

    @_mutmut_mutated(mutants_xǁAliasMapǁ_compute_alias_candidates__mutmut)
    def _compute_alias_candidates(self, field_info: FieldInfo) -> list[str]:
        if validation_alias := field_info.validation_alias:
            return self._resolve_alias(validation_alias)
        return []

    def xǁAliasMapǁ_compute_alias_candidates__mutmut_orig(self, field_info: FieldInfo) -> list[str]:
        if validation_alias := field_info.validation_alias:
            return self._resolve_alias(validation_alias)
        return []

    def xǁAliasMapǁ_compute_alias_candidates__mutmut_1(self, field_info: FieldInfo) -> list[str]:
        if validation_alias := field_info.validation_alias:
            return self._resolve_alias(None)
        return []

    @staticmethod
    @_mutmut_mutated(mutants_xǁAliasMapǁ_resolve_alias__mutmut)
    def _resolve_alias(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_orig(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_1(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_2(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_3(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_4(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                None
            ):
                return choices
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_5(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = None
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_6(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "XXUnable to resolve alias. XX"
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_7(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_8(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "UNABLE TO RESOLVE ALIAS. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(msg)

    @staticmethod
    def xǁAliasMapǁ_resolve_alias__mutmut_9(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises NotImplementedError for AliasPath and AliasChoices/AliasPath objects.
        """
        match alias:
            case str():
                return [alias]
            case AliasChoices(choices=choices) if all(
                isinstance(choice, str) for choice in choices
            ):
                return choices
            case _:
                msg = (
                    "Unable to resolve alias. "
                    f"Expected str or AliasChoices of str, got '{alias}'."
                )
                raise NotImplementedError(None)

mutants_xǁAliasMapǁ__init____mutmut['_mutmut_orig'] = AliasMap.xǁAliasMapǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_1'] = AliasMap.xǁAliasMapǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_2'] = AliasMap.xǁAliasMapǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_3'] = AliasMap.xǁAliasMapǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_4'] = AliasMap.xǁAliasMapǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_5'] = AliasMap.xǁAliasMapǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_6'] = AliasMap.xǁAliasMapǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ__init____mutmut['xǁAliasMapǁ__init____mutmut_7'] = AliasMap.xǁAliasMapǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁAliasMapǁ_generate_alias_map__mutmut['_mutmut_orig'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_1'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_2'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_3'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_4'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_5'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_6'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_7'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_8'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_9'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_10'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_11'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_12'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_13'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_14'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_15'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_16'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_17'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_18'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_19'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_20'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_21'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_22'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_23'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_24'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_25'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_26'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_27'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_generate_alias_map__mutmut['xǁAliasMapǁ_generate_alias_map__mutmut_28'] = AliasMap.xǁAliasMapǁ_generate_alias_map__mutmut_28 # type: ignore # mutmut generated

mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['_mutmut_orig'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_1'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_2'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_3'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_4'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_5'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_6'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_7'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_8'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_9'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_10'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_11'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_12'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_13'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_14'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_15'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_16'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_17'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_18'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_19'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_20'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_21'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_22'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_23'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_24'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_25'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_26'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_27'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_28'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_29'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_30'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_31'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_32'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_33'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_34'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_35'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_36'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_37'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_38'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_39'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_40'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_41'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_42'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_43'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_44'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_45'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_46'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_47'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_48'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_49'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_50'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_51'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_52'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_53'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_54'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_get_alias_resolver__mutmut['xǁAliasMapǁ_get_alias_resolver__mutmut_55'] = AliasMap.xǁAliasMapǁ_get_alias_resolver__mutmut_55 # type: ignore # mutmut generated

mutants_xǁAliasMapǁ_compute_alias_candidates__mutmut['_mutmut_orig'] = AliasMap.xǁAliasMapǁ_compute_alias_candidates__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_compute_alias_candidates__mutmut['xǁAliasMapǁ_compute_alias_candidates__mutmut_1'] = AliasMap.xǁAliasMapǁ_compute_alias_candidates__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAliasMapǁ_resolve_alias__mutmut['_mutmut_orig'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_1'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_2'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_3'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_4'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_5'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_6'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_7'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_8'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAliasMapǁ_resolve_alias__mutmut['xǁAliasMapǁ_resolve_alias__mutmut_9'] = AliasMap.xǁAliasMapǁ_resolve_alias__mutmut_9 # type: ignore # mutmut generated
