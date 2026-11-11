from pydantic import BaseModel
from typing_extensions import TypeForm


class MissingGroupByError(Exception):
    def __init__(self, model: type[BaseModel]) -> None:
        self.model = model

        super().__init__(model)

    def __str__(self) -> str:
        return (
            f"Model '{self.model.__name__}' with aggregation target "
            "does not specify ConfigDict.group_by."
        )


class InvalidGroupByError(Exception):
    def __init__(self, model: type[BaseModel], group_by_value: str) -> None:
        self.model = model
        self.group_by_value = group_by_value

        super().__init__(model, group_by_value)

    def __str__(self) -> str:
        return (
            f"Invalid grouping key '{self.group_by_value}' "
            f"for '{self.model.__name__}'. "
            "Grouping keys must reference scalar model fields."
        )


class MissingDiscriminatorError(Exception):
    def __init__(self, type_form: TypeForm) -> None:
        self.type_form = type_form

        super().__init__(type_form)

    def __str__(self) -> str:
        return (
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{self.type_form}'."
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

        super().__init__(field_name, model, aliases, projection)

    def __str__(self) -> str:
        reason: str = (
            f"None of computed aliases '{self.aliases}' "
            f"in input data projection '{self.projection}'."
            if self.projection
            else "Empty or missing input data projection."
        )
        return (
            f"Unable to resolve AliasChoice for field '{self.field_name}' "
            f"of model '{self.model.__name__}': {reason}"
        )
