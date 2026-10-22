from dataclasses import dataclass
from typing import Annotated

import polars as pl
import pytest
from graphty import Aggregation, ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel

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


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params: list[Parameter] = [
    Parameter(
        model=CoalesceModel,
        data=coalesce_data,
        bindings=snapshot([{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": None}]),
        model_dump=snapshot([{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": None}]),
    ),
    Parameter(
        model=ConcatenateModel,
        data=concatenate_data,
        bindings=snapshot(
            [{"x": 1, "string": "hello, world"}, {"x": 2, "string": "hello, graphty"}]
        ),
        model_dump=snapshot(
            [{"x": 1, "string": "hello, world"}, {"x": 2, "string": "hello, graphty"}]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_reduce_aggregation(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
