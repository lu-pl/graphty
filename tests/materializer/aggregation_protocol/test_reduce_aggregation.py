from typing import Annotated

import pytest
from graphty import ConfigDict, ModelMaterializer, Reduce
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter

data = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 1, "y": 3, "z": 4},
    {"x": 2, "y": 4, "z": 5},
]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: int


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[float, Reduce()]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[float, Reduce("mean")]


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested3: Model3


class Model5(BaseModel):
    x: int
    nested3: Model3


class Model6(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested4: Model4


class Model7(BaseModel):
    nested4: Model4


params = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected([{"x": 1, "y": 2}, {"x": 2, "y": 4}]),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected([{"x": 1, "y": 2}, {"x": 2, "y": 4}]),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected([{"x": 1, "y": 2.5}, {"x": 2, "y": 4.0}]),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested3": {"x": 1, "y": 2.5}},
                {"x": 2, "nested3": {"x": 2, "y": 4.0}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested3": {"x": 1, "y": 2.5}},
                {"x": 1, "nested3": {"x": 1, "y": 2.5}},
                {"x": 2, "nested3": {"x": 2, "y": 4.0}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested4": {"x": 1, "nested3": {"x": 1, "y": 2.5}}},
                {"x": 2, "nested4": {"x": 2, "nested3": {"x": 2, "y": 4.0}}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=Expected(
            [
                {"nested4": {"x": 1, "nested3": {"x": 1, "y": 2.5}}},
                {"nested4": {"x": 1, "nested3": {"x": 1, "y": 2.5}}},
                {"nested4": {"x": 2, "nested3": {"x": 2, "y": 4.0}}},
            ]
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
