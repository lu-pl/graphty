from dataclasses import dataclass

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, Field

data = [
    {"a": 1, "b": 3},
    {"a": 1, "b": 4},
    {"a": 2, "b": 6},
]


class Model1(BaseModel):
    x: int = Field(validation_alias="a")
    y: int = Field(validation_alias="b")


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int = Field(validation_alias="a")
    y: list[int] = Field(validation_alias="b")


class Model3(BaseModel):
    nested_1: Model1
    nested_2: Model2


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")
    x: int = Field(validation_alias="a", exclude=True)

    agg_1: list[Model1]
    agg_2: list[Model2]
    agg_3: list[Model3]


class Model5(BaseModel):
    x: int = Field(validation_alias=AliasChoices("foo", "bar", "a"))
    y: int = Field(validation_alias=AliasChoices("foo", "bar", "b"))


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
        bindings=snapshot([{"a": 1, "b": 3}, {"a": 1, "b": 4}, {"a": 2, "b": 6}]),
        model_dump=snapshot([{"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 2, "y": 6}]),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot([{"a": 1, "b": [3, 4]}, {"a": 2, "b": [6]}]),
        model_dump=snapshot([{"x": 1, "y": [3, 4]}, {"x": 2, "y": [6]}]),
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=snapshot(
            [
                {"nested_1": {"a": 1, "b": 3}, "nested_2": {"a": 1, "b": [3, 4]}},
                {"nested_1": {"a": 1, "b": 4}, "nested_2": {"a": 1, "b": [3, 4]}},
                {"nested_1": {"a": 2, "b": 6}, "nested_2": {"a": 2, "b": [6]}},
            ]
        ),
        model_dump=snapshot(
            [
                {"nested_1": {"x": 1, "y": 3}, "nested_2": {"x": 1, "y": [3, 4]}},
                {"nested_1": {"x": 1, "y": 4}, "nested_2": {"x": 1, "y": [3, 4]}},
                {"nested_1": {"x": 2, "y": 6}, "nested_2": {"x": 2, "y": [6]}},
            ]
        ),
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=snapshot(
            [
                {
                    "a": 1,
                    "agg_1": [{"a": 1, "b": 3}, {"a": 1, "b": 4}],
                    "agg_2": [{"a": 1, "b": [3, 4]}],
                    "agg_3": [
                        {
                            "nested_1": {"a": 1, "b": 3},
                            "nested_2": {"a": 1, "b": [3, 4]},
                        },
                        {
                            "nested_1": {"a": 1, "b": 4},
                            "nested_2": {"a": 1, "b": [3, 4]},
                        },
                    ],
                },
                {
                    "a": 2,
                    "agg_1": [{"a": 2, "b": 6}],
                    "agg_2": [{"a": 2, "b": [6]}],
                    "agg_3": [
                        {"nested_1": {"a": 2, "b": 6}, "nested_2": {"a": 2, "b": [6]}}
                    ],
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "agg_1": [{"x": 1, "y": 3}, {"x": 1, "y": 4}],
                    "agg_2": [{"x": 1, "y": [3, 4]}],
                    "agg_3": [
                        {
                            "nested_1": {"x": 1, "y": 3},
                            "nested_2": {"x": 1, "y": [3, 4]},
                        },
                        {
                            "nested_1": {"x": 1, "y": 4},
                            "nested_2": {"x": 1, "y": [3, 4]},
                        },
                    ],
                },
                {
                    "agg_1": [{"x": 2, "y": 6}],
                    "agg_2": [{"x": 2, "y": [6]}],
                    "agg_3": [
                        {"nested_1": {"x": 2, "y": 6}, "nested_2": {"x": 2, "y": [6]}}
                    ],
                },
            ]
        ),
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=snapshot([{"a": 1, "b": 3}, {"a": 1, "b": 4}, {"a": 2, "b": 6}]),
        model_dump=snapshot([{"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 2, "y": 6}]),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_basic_aliasing(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
