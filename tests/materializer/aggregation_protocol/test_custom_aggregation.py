from typing import Annotated

import polars as pl
import pytest
from graphty import Aggregation, ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


class Coalesce(Aggregation):
    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().first()


type CoalescedOptionalInt = Annotated[
    int | None | list[int],
    """Actually int | None.
    list[int] is for triggering the graphty aggregation code path.
    Note that this is a contrived example and a workaround.
    """,
]

coalesce_data = [
    {"x": 1, "y": None},
    {"x": 1, "y": 1},
    {"x": 2, "y": None},
    {"x": 2, "y": 2},
    {"x": 3, "y": None},
]


class CoalesceModel(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[CoalescedOptionalInt, Coalesce()]


class Concatenate(Aggregation):
    def __init__(self, separator: str = ", ") -> None:
        self.separator = separator

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().implode().list.join(self.separator)


concatenate_data = [
    {"x": 1, "string": "hello"},
    {"x": 1, "string": "world"},
    {"x": 2, "string": "hello"},
    {"x": 2, "string": "graphty"},
]


type ConcatenatedStr = Annotated[
    str | list[str],
    """Actually str.
    list[str] is for triggering the graphty aggregation code path.
    Note that this is a contrived example and a workaround.
    """,
]


class ConcatenateModel(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    string: Annotated[ConcatenatedStr, Concatenate()]


params: list[Parameter] = [
    Parameter(
        kwargs={"model": CoalesceModel, "data": coalesce_data},
        expected=Expected([{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": None}]),
    ),
    Parameter(
        kwargs={"model": ConcatenateModel, "data": concatenate_data},
        expected=Expected(
            [{"x": 1, "string": "hello, world"}, {"x": 2, "string": "hello, graphty"}]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_reduce_aggregation(param):
    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
