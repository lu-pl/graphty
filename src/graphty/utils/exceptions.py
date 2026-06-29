from pydantic import BaseModel
from typing_extensions import TypeForm


class MissingGroupByError(Exception):
    def __init__(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "does not specify ConfigDict.group_by."
        )


class MissingDiscriminatorError(Exception):
    def __init__(self, type_form: TypeForm) -> None:
        super().__init__(
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )
