from typing import Annotated

import pytest
from graphty import Collect, ConfigDict, ModelMaterializer, Reduce
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter

data = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 1, "y": 3, "z": 4},
    {"x": 1, "y": 3, "z": 5},
    {"x": 1, "y": None, "z": 6},
    {"x": 2, "y": 4, "z": 7},
]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: list[int]
    z: int  # implicit first


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: list[int]
    z: Annotated[float, Reduce("mean")]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[list[int], Collect(unique=False)]
    z: Annotated[float, Reduce("mean")]


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[list[int | None], Collect(unique=False, drop_nulls=False)]
    z: Annotated[float, Reduce("mean")]


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested1: Model1
    nested2: Model2
    nested3: Model3
    nested4: Model4


class Model6(BaseModel):
    nested1: Model1
    nested2: Model2
    nested3: Model3
    nested4: Model4


class Model7(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested5: Model5


class Model8(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested6: Model6


class Model9(BaseModel):
    nested5: Model5


class Model10(BaseModel):
    nested6: Model6


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected([{"x": 1, "y": [2, 3], "z": 3}, {"x": 2, "y": [4], "z": 7}]),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            [{"x": 1, "y": [2, 3], "z": 4.5}, {"x": 2, "y": [4], "z": 7.0}]
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            [{"x": 1, "y": [2, 3, 3], "z": 4.5}, {"x": 2, "y": [4], "z": 7.0}]
        ),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            [{"x": 1, "y": [2, 3, 3, None], "z": 4.5}, {"x": 2, "y": [4], "z": 7.0}]
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            [
                {
                    "x": 1,
                    "nested1": {"x": 1, "y": [2, 3], "z": 3},
                    "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                    "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                    "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                },
                {
                    "x": 2,
                    "nested1": {"x": 2, "y": [4], "z": 7},
                    "nested2": {"x": 2, "y": [4], "z": 7.0},
                    "nested3": {"x": 2, "y": [4], "z": 7.0},
                    "nested4": {"x": 2, "y": [4], "z": 7.0},
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            [
                {
                    "nested1": {"x": 1, "y": [2, 3], "z": 3},
                    "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                    "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                    "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                },
                {
                    "nested1": {"x": 1, "y": [2, 3], "z": 3},
                    "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                    "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                    "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                },
                {
                    "nested1": {"x": 1, "y": [2, 3], "z": 3},
                    "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                    "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                    "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                },
                {
                    "nested1": {"x": 1, "y": [2, 3], "z": 3},
                    "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                    "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                    "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                },
                {
                    "nested1": {"x": 2, "y": [4], "z": 7},
                    "nested2": {"x": 2, "y": [4], "z": 7.0},
                    "nested3": {"x": 2, "y": [4], "z": 7.0},
                    "nested4": {"x": 2, "y": [4], "z": 7.0},
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=Expected(
            [
                {
                    "x": 1,
                    "nested5": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    },
                },
                {
                    "x": 2,
                    "nested5": {
                        "x": 2,
                        "nested1": {"x": 2, "y": [4], "z": 7},
                        "nested2": {"x": 2, "y": [4], "z": 7.0},
                        "nested3": {"x": 2, "y": [4], "z": 7.0},
                        "nested4": {"x": 2, "y": [4], "z": 7.0},
                    },
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model8, "data": data},
        expected=Expected(
            [
                {
                    "x": 1,
                    "nested6": {
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    },
                },
                {
                    "x": 2,
                    "nested6": {
                        "nested1": {"x": 2, "y": [4], "z": 7},
                        "nested2": {"x": 2, "y": [4], "z": 7.0},
                        "nested3": {"x": 2, "y": [4], "z": 7.0},
                        "nested4": {"x": 2, "y": [4], "z": 7.0},
                    },
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model9, "data": data},
        expected=Expected(
            [
                {
                    "nested5": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested5": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested5": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested5": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested5": {
                        "x": 2,
                        "nested1": {"x": 2, "y": [4], "z": 7},
                        "nested2": {"x": 2, "y": [4], "z": 7.0},
                        "nested3": {"x": 2, "y": [4], "z": 7.0},
                        "nested4": {"x": 2, "y": [4], "z": 7.0},
                    }
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model10, "data": data},
        expected=Expected(
            [
                {
                    "nested6": {
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested6": {
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested6": {
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested6": {
                        "nested1": {"x": 1, "y": [2, 3], "z": 3},
                        "nested2": {"x": 1, "y": [2, 3], "z": 4.5},
                        "nested3": {"x": 1, "y": [2, 3, 3], "z": 4.5},
                        "nested4": {"x": 1, "y": [2, 3, 3, None], "z": 4.5},
                    }
                },
                {
                    "nested6": {
                        "nested1": {"x": 2, "y": [4], "z": 7},
                        "nested2": {"x": 2, "y": [4], "z": 7.0},
                        "nested3": {"x": 2, "y": [4], "z": 7.0},
                        "nested4": {"x": 2, "y": [4], "z": 7.0},
                    }
                },
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
