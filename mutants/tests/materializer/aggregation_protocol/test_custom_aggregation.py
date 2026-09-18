from typing import Annotated

import polars as pl
import pytest
from graphty import Aggregation, ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter

coalesce_data = [
    {"x": 1, "y": None},
    {"x": 1, "y": 1},
    {"x": 2, "y": None},
    {"x": 2, "y": 2},
    {"x": 3, "y": None},
]


class Coalesce(Aggregation):
    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().first()


class CoalesceModel(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[int | None, Coalesce()]


concatenate_data = [
    {"x": 1, "string": "hello"},
    {"x": 1, "string": "world"},
    {"x": 2, "string": "hello"},
    {"x": 2, "string": "graphty"},
]


class Concatenate(Aggregation):
    def __init__(self, separator: str = ", ") -> None:
        self.separator = separator

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().implode().list.join(self.separator)


class ConcatenateModel(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    string: Annotated[str, Concatenate()]


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
