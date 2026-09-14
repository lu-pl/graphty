import abc
from collections.abc import Callable, Iterator
from functools import reduce

import polars as pl


class Aggregation(abc.ABC):
    @abc.abstractmethod
    def __call__(self, expr: pl.Expr) -> pl.Expr: ...


class Reduce(Aggregation):
    def __init__(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(expr, **self.kwargs)


class Collect(Aggregation):
    def __init__(self, unique: bool = True, drop_nulls: bool = True) -> None:
        self.unique = unique
        self.drop_nulls = drop_nulls

    def __iter__(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: expr.unique()
        if self.drop_nulls:
            yield lambda expr: expr.drop_nulls()

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, expr)
