from collections import UserDict
from collections.abc import Callable, Iterator
from types import resolve_bases

from pydantic import AliasChoices, BaseModel
from pydantic.fields import FieldInfo


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

    def __init__(self, model: type[BaseModel], projection: set[str]) -> None:
        self.model = model
        self.projection = projection

        self.data = dict(self._generate_alias_map())

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
                        msg = (
                            f"Unable to resolve AliasChoice for field '{k}' of model '{self.model.__name__}'.\n"
                            f"None of computed aliases '{aliases}' in projection '{self.projection}'."
                        )
                        raise ValueError(msg)

                    yield (k, alias)
                case _:  # pragma: no cover; unreachable
                    assert False, "This should never happen."

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
            case True, False:  # TODO: trigger in tests
                return lambda field_name, _: [field_name]
            case False, True:
                return lambda _, field_info: self._compute_alias_candidates(
                    field_info=field_info
                )
            case True, True:  # TODO: trigger in tests
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

    def _compute_alias_candidates(self, field_info: FieldInfo) -> list[str]:
        if (validation_alias := field_info.validation_alias):
            return self._resolve_alias(validation_alias)
        return []
        
    @staticmethod
    def _resolve_alias(alias: str | AliasChoices) -> list[str]:
        """Helper for resolving alias/validation_alias values in FieldInfo objects.

        Note that pydantic.AliasPath is not meaningful in the context of flat relational binding mappings;
        the method therefore raises an Exception for AliasPath and AliasChoices/AliasPath objects.
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
                raise ValueError(msg)
