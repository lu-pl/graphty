from pydantic import BaseModel
from typing_extensions import TypeForm


class MissingGroupByError(Exception):
    def __init__(self, model: type[BaseModel]) -> None:
        self.model = model

        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "does not specify ConfigDict.group_by."
        )


class InvalidGroupByError(Exception):
    def __init__(self, model: type[BaseModel], group_by_value: str) -> None:
        self.model = model
        self.group_by_value = group_by_value

        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "Grouping keys must reference scalar model fields."
        )


class MissingDiscriminatorError(Exception):
    def __init__(self, type_form: TypeForm) -> None:
        self.type_form = type_form

        super().__init__(
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )


class AliasResolutionError(Exception):
    def __init__(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        self.field_name = field_name
        self.model = model
        self.aliases = aliases
        self.projection = projection

        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "Empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
