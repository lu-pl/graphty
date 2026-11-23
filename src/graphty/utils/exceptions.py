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
