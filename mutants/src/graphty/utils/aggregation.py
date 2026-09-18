import abc
from collections.abc import Callable, Iterator
from functools import reduce

import polars as pl


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class Aggregation(abc.ABC):
    @abc.abstractmethod
    def __call__(self, expr: pl.Expr) -> pl.Expr: ...
mutants_xǁReduceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReduceǁ__call____mutmut: MutantDict = {}  # type: ignore


class Reduce(Aggregation):
    @_mutmut_mutated(mutants_xǁReduceǁ__init____mutmut)
    def __init__(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_orig(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_1(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = None
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_2(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if (isinstance(reduction, str)) and False else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_3(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if (isinstance(reduction, str)) or True else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_4(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(None, reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_5(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, None) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_6(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_7(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, ) if isinstance(reduction, str) else reduction
        )
        self.kwargs = kwargs
    def xǁReduceǁ__init____mutmut_8(
        self, reduction: str | Callable[..., pl.Expr] = pl.Expr.first, **kwargs
    ) -> None:
        self.reduction: Callable[..., pl.Expr] = (
            getattr(pl.Expr, reduction) if isinstance(reduction, str) else reduction
        )
        self.kwargs = None

    @_mutmut_mutated(mutants_xǁReduceǁ__call____mutmut)
    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(expr, **self.kwargs)

    def xǁReduceǁ__call____mutmut_orig(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(expr, **self.kwargs)

    def xǁReduceǁ__call____mutmut_1(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(None, **self.kwargs)

    def xǁReduceǁ__call____mutmut_2(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(**self.kwargs)

    def xǁReduceǁ__call____mutmut_3(self, expr: pl.Expr) -> pl.Expr:
        return self.reduction(expr, )

mutants_xǁReduceǁ__init____mutmut['_mutmut_orig'] = Reduce.xǁReduceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_1'] = Reduce.xǁReduceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_2'] = Reduce.xǁReduceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_3'] = Reduce.xǁReduceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_4'] = Reduce.xǁReduceǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_5'] = Reduce.xǁReduceǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_6'] = Reduce.xǁReduceǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_7'] = Reduce.xǁReduceǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁReduceǁ__init____mutmut['xǁReduceǁ__init____mutmut_8'] = Reduce.xǁReduceǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁReduceǁ__call____mutmut['_mutmut_orig'] = Reduce.xǁReduceǁ__call____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReduceǁ__call____mutmut['xǁReduceǁ__call____mutmut_1'] = Reduce.xǁReduceǁ__call____mutmut_1 # type: ignore # mutmut generated
mutants_xǁReduceǁ__call____mutmut['xǁReduceǁ__call____mutmut_2'] = Reduce.xǁReduceǁ__call____mutmut_2 # type: ignore # mutmut generated
mutants_xǁReduceǁ__call____mutmut['xǁReduceǁ__call____mutmut_3'] = Reduce.xǁReduceǁ__call____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCollectǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCollectǁ__iter____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCollectǁ__call____mutmut: MutantDict = {}  # type: ignore


class Collect(Aggregation):
    @_mutmut_mutated(mutants_xǁCollectǁ__init____mutmut)
    def __init__(self, unique: bool = True, drop_nulls: bool = True) -> None:
        self.unique = unique
        self.drop_nulls = drop_nulls
    def xǁCollectǁ__init____mutmut_orig(self, unique: bool = True, drop_nulls: bool = True) -> None:
        self.unique = unique
        self.drop_nulls = drop_nulls
    def xǁCollectǁ__init____mutmut_1(self, unique: bool = False, drop_nulls: bool = True) -> None:
        self.unique = unique
        self.drop_nulls = drop_nulls
    def xǁCollectǁ__init____mutmut_2(self, unique: bool = True, drop_nulls: bool = False) -> None:
        self.unique = unique
        self.drop_nulls = drop_nulls
    def xǁCollectǁ__init____mutmut_3(self, unique: bool = True, drop_nulls: bool = True) -> None:
        self.unique = None
        self.drop_nulls = drop_nulls
    def xǁCollectǁ__init____mutmut_4(self, unique: bool = True, drop_nulls: bool = True) -> None:
        self.unique = unique
        self.drop_nulls = None

    @_mutmut_mutated(mutants_xǁCollectǁ__iter____mutmut)
    def __iter__(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: expr.unique()
        if self.drop_nulls:
            yield lambda expr: expr.drop_nulls()

    def xǁCollectǁ__iter____mutmut_orig(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: expr.unique()
        if self.drop_nulls:
            yield lambda expr: expr.drop_nulls()

    def xǁCollectǁ__iter____mutmut_1(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: None
        if self.drop_nulls:
            yield lambda expr: expr.drop_nulls()

    def xǁCollectǁ__iter____mutmut_2(self) -> Iterator[Callable[[pl.Expr], pl.Expr]]:
        if self.unique:
            yield lambda expr: expr.unique()
        if self.drop_nulls:
            yield lambda expr: None

    @_mutmut_mutated(mutants_xǁCollectǁ__call____mutmut)
    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, expr)

    def xǁCollectǁ__call____mutmut_orig(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, expr)

    def xǁCollectǁ__call____mutmut_1(self, expr: pl.Expr) -> pl.Expr:
        return reduce(None, self, expr)

    def xǁCollectǁ__call____mutmut_2(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), None, expr)

    def xǁCollectǁ__call____mutmut_3(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, None)

    def xǁCollectǁ__call____mutmut_4(self, expr: pl.Expr) -> pl.Expr:
        return reduce(self, expr)

    def xǁCollectǁ__call____mutmut_5(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), expr)

    def xǁCollectǁ__call____mutmut_6(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(x), self, )

    def xǁCollectǁ__call____mutmut_7(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: None, self, expr)

    def xǁCollectǁ__call____mutmut_8(self, expr: pl.Expr) -> pl.Expr:
        return reduce(lambda x, y: y(None), self, expr)

mutants_xǁCollectǁ__init____mutmut['_mutmut_orig'] = Collect.xǁCollectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCollectǁ__init____mutmut['xǁCollectǁ__init____mutmut_1'] = Collect.xǁCollectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCollectǁ__init____mutmut['xǁCollectǁ__init____mutmut_2'] = Collect.xǁCollectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCollectǁ__init____mutmut['xǁCollectǁ__init____mutmut_3'] = Collect.xǁCollectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCollectǁ__init____mutmut['xǁCollectǁ__init____mutmut_4'] = Collect.xǁCollectǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁCollectǁ__iter____mutmut['_mutmut_orig'] = Collect.xǁCollectǁ__iter____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCollectǁ__iter____mutmut['xǁCollectǁ__iter____mutmut_1'] = Collect.xǁCollectǁ__iter____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCollectǁ__iter____mutmut['xǁCollectǁ__iter____mutmut_2'] = Collect.xǁCollectǁ__iter____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCollectǁ__call____mutmut['_mutmut_orig'] = Collect.xǁCollectǁ__call____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_1'] = Collect.xǁCollectǁ__call____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_2'] = Collect.xǁCollectǁ__call____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_3'] = Collect.xǁCollectǁ__call____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_4'] = Collect.xǁCollectǁ__call____mutmut_4 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_5'] = Collect.xǁCollectǁ__call____mutmut_5 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_6'] = Collect.xǁCollectǁ__call____mutmut_6 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_7'] = Collect.xǁCollectǁ__call____mutmut_7 # type: ignore # mutmut generated
mutants_xǁCollectǁ__call____mutmut['xǁCollectǁ__call____mutmut_8'] = Collect.xǁCollectǁ__call____mutmut_8 # type: ignore # mutmut generated
