from collections.abc import Callable, Iterator
from dataclasses import dataclass
from functools import reduce

import polars as pl
from pydantic import ConfigDict as PydanticConfigDict


class ConfigDict(PydanticConfigDict):
    group_by: str


@dataclass
class Agg:
    """Configuration class for aggregation fields.

    The class allows to configure aggregation behavior for
    model fields with aggretation targets:

    E.g. `field: typing.Annotated[list[int], Agg(unique=False)]`
    will aggregate non-unique values of a given partition into `field`.

    Note: This is a draft and likely subject of breaking API changes.
    """

    unique: bool = True
    drop_nulls: bool = True

    def __iter__(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: expr.unique()
        if self.drop_nulls:
            yield lambda expr: expr.drop_nulls()

    def apply_to(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, expr)


class Opaque:
    """Type for marking a field as opaque for the planner.

    For Pydantic fields typed with `Annotated[<type>, Opaque()]`
    the GraphTy planner will forward the entire projection as a pl.Struct
    and otherwise ignore that field.

    Disengaging the planner for a field with `Opaque`
    allows a before-validator to act on the raw bindings on the Python level.
    """
