import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Field
from tests.materializer.param import Expected, Parameter

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


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            bindings=[{"a": 1}, {"a": 2}, {"a": 3}],
            model_dump=[
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            bindings=[{"a": 1}, {"a": 2}, {"a": 3}],
            model_dump=[
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            bindings=[{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}],
            model_dump=[
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            bindings=[
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ],
            model_dump=[
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            bindings=[{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}],
            model_dump=[
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            bindings=[
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ],
            model_dump=[
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": []},
        expected=Expected(
            bindings=[],
            model_dump=[],
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
