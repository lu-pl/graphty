from typing import Annotated

import pytest
from graphty import Collect, ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter

data = [
    {"x": 1, "y": 2},
    {"x": 1, "y": 3},
    {"x": 1, "y": 3},
    {"x": 1, "y": None},
    {"x": 2, "y": 4},
]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: list[int]


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[list[int | None], Collect()]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[list[int | None], Collect(drop_nulls=False)]


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[list[int | None], Collect(drop_nulls=False, unique=False)]


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    agg: list[Model1]


class Model6(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    agg: Annotated[list[Model1], Collect()]


class NestedAgg(BaseModel):
    y: int | None


class Model7(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    agg: list[NestedAgg]


class Model8(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    agg: Annotated[list[NestedAgg], Collect()]


class Model9(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    agg: Annotated[list[NestedAgg], Collect(unique=False)]


class Model10(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested1: Model1
    nested2: Model2
    nested3: Model3
    nested4: Model4
    nested5: Model5
    nested6: Model6
    nested7: Model7
    nested8: Model8
    nested9: Model9


class Model11(BaseModel):
    nested1: Model1
    nested2: Model2
    nested3: Model3
    nested4: Model4
    nested5: Model5
    nested6: Model6
    nested7: Model7
    nested8: Model8
    nested9: Model9


class Model12(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested10: Model10
    nested11: Model11


class Model13(BaseModel):
    nested10: Model10
    nested11: Model11


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected([{"x": 1, "y": [2, 3]}, {"x": 2, "y": [4]}]),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected([{"x": 1, "y": [2, 3]}, {"x": 2, "y": [4]}]),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected([{"x": 1, "y": [2, 3, None]}, {"x": 2, "y": [4]}]),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected([{"x": 1, "y": [2, 3, 3, None]}, {"x": 2, "y": [4]}]),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            [
                {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                {"x": 2, "agg": [{"x": 2, "y": [4]}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            [
                {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                {"x": 2, "agg": [{"x": 2, "y": [4]}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=Expected(
            [
                {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                {"x": 2, "agg": [{"y": 4}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model8, "data": data},
        expected=Expected(
            [
                {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                {"x": 2, "agg": [{"y": 4}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model9, "data": data},
        expected=Expected(
            [
                {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}]},
                {"x": 2, "agg": [{"y": 4}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model10, "data": data},
        expected=Expected(
            [
                {
                    "x": 1,
                    "nested1": {"x": 1, "y": [2, 3]},
                    "nested2": {"x": 1, "y": [2, 3]},
                    "nested3": {"x": 1, "y": [2, 3, None]},
                    "nested4": {"x": 1, "y": [2, 3, 3, None]},
                    "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested9": {
                        "x": 1,
                        "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                    },
                },
                {
                    "x": 2,
                    "nested1": {"x": 2, "y": [4]},
                    "nested2": {"x": 2, "y": [4]},
                    "nested3": {"x": 2, "y": [4]},
                    "nested4": {"x": 2, "y": [4]},
                    "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                    "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                    "nested7": {"x": 2, "agg": [{"y": 4}]},
                    "nested8": {"x": 2, "agg": [{"y": 4}]},
                    "nested9": {"x": 2, "agg": [{"y": 4}]},
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model11, "data": data},
        expected=Expected(
            [
                {
                    "nested1": {"x": 1, "y": [2, 3]},
                    "nested2": {"x": 1, "y": [2, 3]},
                    "nested3": {"x": 1, "y": [2, 3, None]},
                    "nested4": {"x": 1, "y": [2, 3, 3, None]},
                    "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested9": {
                        "x": 1,
                        "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                    },
                },
                {
                    "nested1": {"x": 1, "y": [2, 3]},
                    "nested2": {"x": 1, "y": [2, 3]},
                    "nested3": {"x": 1, "y": [2, 3, None]},
                    "nested4": {"x": 1, "y": [2, 3, 3, None]},
                    "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested9": {
                        "x": 1,
                        "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                    },
                },
                {
                    "nested1": {"x": 1, "y": [2, 3]},
                    "nested2": {"x": 1, "y": [2, 3]},
                    "nested3": {"x": 1, "y": [2, 3, None]},
                    "nested4": {"x": 1, "y": [2, 3, 3, None]},
                    "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested9": {
                        "x": 1,
                        "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                    },
                },
                {
                    "nested1": {"x": 1, "y": [2, 3]},
                    "nested2": {"x": 1, "y": [2, 3]},
                    "nested3": {"x": 1, "y": [2, 3, None]},
                    "nested4": {"x": 1, "y": [2, 3, 3, None]},
                    "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                    "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                    "nested9": {
                        "x": 1,
                        "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                    },
                },
                {
                    "nested1": {"x": 2, "y": [4]},
                    "nested2": {"x": 2, "y": [4]},
                    "nested3": {"x": 2, "y": [4]},
                    "nested4": {"x": 2, "y": [4]},
                    "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                    "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                    "nested7": {"x": 2, "agg": [{"y": 4}]},
                    "nested8": {"x": 2, "agg": [{"y": 4}]},
                    "nested9": {"x": 2, "agg": [{"y": 4}]},
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model12, "data": data},
        expected=Expected(
            [
                {
                    "x": 1,
                    "nested10": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                    "nested11": {
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                },
                {
                    "x": 2,
                    "nested10": {
                        "x": 2,
                        "nested1": {"x": 2, "y": [4]},
                        "nested2": {"x": 2, "y": [4]},
                        "nested3": {"x": 2, "y": [4]},
                        "nested4": {"x": 2, "y": [4]},
                        "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested7": {"x": 2, "agg": [{"y": 4}]},
                        "nested8": {"x": 2, "agg": [{"y": 4}]},
                        "nested9": {"x": 2, "agg": [{"y": 4}]},
                    },
                    "nested11": {
                        "nested1": {"x": 2, "y": [4]},
                        "nested2": {"x": 2, "y": [4]},
                        "nested3": {"x": 2, "y": [4]},
                        "nested4": {"x": 2, "y": [4]},
                        "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested7": {"x": 2, "agg": [{"y": 4}]},
                        "nested8": {"x": 2, "agg": [{"y": 4}]},
                        "nested9": {"x": 2, "agg": [{"y": 4}]},
                    },
                },
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model13, "data": data},
        expected=Expected(
            [
                {
                    "nested10": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                    "nested11": {
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                },
                {
                    "nested10": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                    "nested11": {
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                },
                {
                    "nested10": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                    "nested11": {
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                },
                {
                    "nested10": {
                        "x": 1,
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                    "nested11": {
                        "nested1": {"x": 1, "y": [2, 3]},
                        "nested2": {"x": 1, "y": [2, 3]},
                        "nested3": {"x": 1, "y": [2, 3, None]},
                        "nested4": {"x": 1, "y": [2, 3, 3, None]},
                        "nested5": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested6": {"x": 1, "agg": [{"x": 1, "y": [2, 3]}]},
                        "nested7": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested8": {"x": 1, "agg": [{"y": 2}, {"y": 3}, {"y": None}]},
                        "nested9": {
                            "x": 1,
                            "agg": [{"y": 2}, {"y": 3}, {"y": 3}, {"y": None}],
                        },
                    },
                },
                {
                    "nested10": {
                        "x": 2,
                        "nested1": {"x": 2, "y": [4]},
                        "nested2": {"x": 2, "y": [4]},
                        "nested3": {"x": 2, "y": [4]},
                        "nested4": {"x": 2, "y": [4]},
                        "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested7": {"x": 2, "agg": [{"y": 4}]},
                        "nested8": {"x": 2, "agg": [{"y": 4}]},
                        "nested9": {"x": 2, "agg": [{"y": 4}]},
                    },
                    "nested11": {
                        "nested1": {"x": 2, "y": [4]},
                        "nested2": {"x": 2, "y": [4]},
                        "nested3": {"x": 2, "y": [4]},
                        "nested4": {"x": 2, "y": [4]},
                        "nested5": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested6": {"x": 2, "agg": [{"x": 2, "y": [4]}]},
                        "nested7": {"x": 2, "agg": [{"y": 4}]},
                        "nested8": {"x": 2, "agg": [{"y": 4}]},
                        "nested9": {"x": 2, "agg": [{"y": 4}]},
                    },
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
