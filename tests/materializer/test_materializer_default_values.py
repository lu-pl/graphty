from dataclasses import dataclass

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Field

data = [
    {"a": 1},
    {"a": 2},
    {"a": 3},
]


class Model1(BaseModel):
    a: int
    b: int = 1
    c: int = Field(default_factory=lambda: 2)
    d: int = Field(default_factory=lambda data: 3)


class Model2(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: int = 1
    c: int = Field(default_factory=lambda: 2)
    d: int = Field(default_factory=lambda data: 3)


class Model3(BaseModel):
    nested: Model1


class Model4(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model1


class Model5(BaseModel):
    nested: Model2


class Model6(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model2


class Model7(BaseModel):
    x: int = 1


class Model8(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: list[int] = []
    c: list[int] = Field(default_factory=lambda: [1])
    d: list[int] = Field(default_factory=lambda data: [data["a"]])
    e: list[int] = Field(default=[], alias="x")


class Model9(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: list[int] = []
    c: list[int]


class Model10(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: list[Model8]


class Model11(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model8


grouped_data = [
    {"a": 1},
    {"a": 1},
    {"a": 2},
    {"a": 3},
]


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params: list[Parameter] = [
    Parameter(
        model=Model1,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ]
        ),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ]
        ),
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=snapshot(
            [{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}]
        ),
        model_dump=snapshot(
            [
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=snapshot(
            [{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}]
        ),
        model_dump=snapshot(
            [
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model6,
        data=data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(model=Model7, data=[], bindings=snapshot([]), model_dump=snapshot([])),
    # list-of-scalar fields with defaults and no column in the data (#106)
    Parameter(
        model=Model8,
        data=grouped_data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": [], "c": [1], "d": [1], "e": []},
                {"a": 2, "b": [], "c": [1], "d": [2], "e": []},
                {"a": 3, "b": [], "c": [1], "d": [3], "e": []},
            ]
        ),
    ),
    Parameter(
        model=Model9,
        data=[{"a": 1, "c": 1}, {"a": 1, "c": 2}, {"a": 2, "c": 3}],
        bindings=snapshot([{"a": 1, "c": [1, 2]}, {"a": 2, "c": [3]}]),
        model_dump=snapshot(
            [{"a": 1, "b": [], "c": [1, 2]}, {"a": 2, "b": [], "c": [3]}]
        ),
    ),
    Parameter(
        model=Model10,
        data=grouped_data,
        bindings=snapshot(
            [
                {"a": 1, "nested": [{"a": 1}]},
                {"a": 2, "nested": [{"a": 2}]},
                {"a": 3, "nested": [{"a": 3}]},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": [{"a": 1, "b": [], "c": [1], "d": [1], "e": []}]},
                {"a": 2, "nested": [{"a": 2, "b": [], "c": [1], "d": [2], "e": []}]},
                {"a": 3, "nested": [{"a": 3, "b": [], "c": [1], "d": [3], "e": []}]},
            ]
        ),
    ),
    Parameter(
        model=Model11,
        data=grouped_data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": [], "c": [1], "d": [1], "e": []}},
                {"a": 2, "nested": {"a": 2, "b": [], "c": [1], "d": [2], "e": []}},
                {"a": 3, "nested": {"a": 3, "b": [], "c": [1], "d": [3], "e": []}},
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_default_values(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
