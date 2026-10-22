from dataclasses import dataclass
from typing import Annotated

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Field


class DeeplyNested(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int = Field(exclude=True)
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


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


expected_bindings = snapshot(
    [
        {
            "x": 1,
            "model": {"x": 1, "y": [2, 3]},
            "aggr": [
                {"y": 2, "deeply_nested": {"x": 1, "y": [2, 3]}},
                {"y": 3, "deeply_nested": {"x": 1, "y": [2, 3]}},
            ],
        },
        {
            "x": 3,
            "model": {"x": 3, "y": [4]},
            "aggr": [{"y": 4, "deeply_nested": {"x": 3, "y": [4]}}],
        },
    ]
)
expected_model_dump = snapshot(
    [
        {
            "x": 1,
            "model": {"y": [2, 3]},
            "aggr": [
                {"y": 2, "deeply_nested": {"y": [2, 3]}},
                {"y": 3, "deeply_nested": {"y": [2, 3]}},
            ],
        },
        {"x": 3, "model": {"y": [4]}, "aggr": [{"y": 4, "deeply_nested": {"y": [4]}}]},
    ]
)

params: list[Parameter] = [
    Parameter(
        model=Model1,
        data=data,
        bindings=expected_bindings,
        model_dump=expected_model_dump,
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=expected_bindings,
        model_dump=expected_model_dump,
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=expected_bindings,
        model_dump=expected_model_dump,
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=expected_bindings,
        model_dump=expected_model_dump,
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=expected_bindings,
        model_dump=expected_model_dump,
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_grouped_nested(param):

    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
