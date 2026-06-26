from typing import Annotated

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


class DeeplyNested(BaseModel):
    model_config = ConfigDict(group_by="x")

    y: list[int]


class Nested(BaseModel):
    y: int
    deeply_nested: DeeplyNested


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Nested]


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Nested | None]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: Annotated[list[Nested | None], ""]


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Annotated[Nested | None, ""]]


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: Annotated[list[Annotated[Nested | None, ""]], ""]


data = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 3, "y": 4}]

expected = [
    {
        "x": 1,
        "model": {"y": [2, 3]},
        "aggr": [
            {"y": 2, "deeply_nested": {"y": [2, 3]}},
            {"y": 3, "deeply_nested": {"y": [2, 3]}},
        ],
    },
    {
        "x": 3,
        "model": {"y": [4]},
        "aggr": [{"y": 4, "deeply_nested": {"y": [4]}}],
    },
]


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data}, expected=Expected(bindings=expected)
    ),
    Parameter(
        kwargs={"model": Model2, "data": data}, expected=Expected(bindings=expected)
    ),
    Parameter(
        kwargs={"model": Model3, "data": data}, expected=Expected(bindings=expected)
    ),
    Parameter(
        kwargs={"model": Model4, "data": data}, expected=Expected(bindings=expected)
    ),
    Parameter(
        kwargs={"model": Model5, "data": data}, expected=Expected(bindings=expected)
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_grouped_nested(param):

    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
