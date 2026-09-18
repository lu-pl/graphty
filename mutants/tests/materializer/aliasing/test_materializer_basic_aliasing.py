import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import AliasChoices, BaseModel, Field
from tests.materializer.param import Expected, Parameter

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


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            bindings=[{"a": 1, "b": 3}, {"a": 1, "b": 4}, {"a": 2, "b": 6}],
            model_dump=[{"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 2, "y": 6}],
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            bindings=[{"a": 1, "b": [3, 4]}, {"a": 2, "b": [6]}],
            model_dump=[{"x": 1, "y": [3, 4]}, {"x": 2, "y": [6]}],
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            bindings=[
                {"nested_1": {"a": 1, "b": 3}, "nested_2": {"a": 1, "b": [3, 4]}},
                {"nested_1": {"a": 1, "b": 4}, "nested_2": {"a": 1, "b": [3, 4]}},
                {"nested_1": {"a": 2, "b": 6}, "nested_2": {"a": 2, "b": [6]}},
            ],
            model_dump=[
                {"nested_1": {"x": 1, "y": 3}, "nested_2": {"x": 1, "y": [3, 4]}},
                {"nested_1": {"x": 1, "y": 4}, "nested_2": {"x": 1, "y": [3, 4]}},
                {"nested_1": {"x": 2, "y": 6}, "nested_2": {"x": 2, "y": [6]}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            bindings=[
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
            ],
            model_dump=[
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
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            bindings=[{"a": 1, "b": 3}, {"a": 1, "b": 4}, {"a": 2, "b": 6}],
            model_dump=[{"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 2, "y": 6}],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_basic_aliasing(param):
    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
