from pydantic import ConfigDict as PydanticConfigDict


class ConfigDict(PydanticConfigDict):
    group_by: str


class Opaque:
    """Type for marking a field as opaque to the planner.

    For Pydantic fields typed with `Annotated[<type>, Opaque()]`,
    the GraphTy planner will forward the entire projection as a pl.Struct
    and otherwise ignore that field.

    Disengaging the planner for a field with `Opaque`
    allows a before-validator to act on the raw bindings on the Python level.
    """
