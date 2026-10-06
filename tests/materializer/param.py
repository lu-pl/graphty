from collections.abc import Iterable
from dataclasses import dataclass
from re import Pattern


@dataclass
class Expected:
    bindings: list[dict[str, object]]
    model_dump: list[dict[str, object]] | None = None

    def __post_init__(self):
        if self.model_dump is None:
            self.model_dump = self.bindings


@dataclass
class ExpectedException:
    exception: Exception
    match: str | Pattern | None = None


@dataclass
class Parameter:
    kwargs: dict[str, object]
    expected: Expected | ExpectedException | Iterable[Expected | ExpectedException]
