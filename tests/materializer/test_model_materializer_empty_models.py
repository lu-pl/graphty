import pytest
from graphty import ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


class Model1(BaseModel):
    pass


class Model2(BaseModel):
    nested: Model1


class Model3(BaseModel):
    nested: Model2


data = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 1, "y": 3, "z": 4},
    {"x": 2, "y": 4, "z": 5},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            bindings=[
                {"x": 1, "y": 2, "z": 3},
                {"x": 1, "y": 3, "z": 4},
                {"x": 2, "y": 4, "z": 5},
            ],
            model_dump=[{}, {}, {}],
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"y": 2, "x": 1, "z": 3}},
                {"nested": {"y": 3, "x": 1, "z": 4}},
                {"nested": {"y": 4, "x": 2, "z": 5}},
            ],
            model_dump=[{"nested": {}}, {"nested": {}}, {"nested": {}}],
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"nested": {"y": 2, "x": 1, "z": 3}}},
                {"nested": {"nested": {"y": 3, "x": 1, "z": 4}}},
                {"nested": {"nested": {"y": 4, "x": 2, "z": 5}}},
            ],
            model_dump=[
                {"nested": {"nested": {}}},
                {"nested": {"nested": {}}},
                {"nested": {"nested": {}}},
            ],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_empty_models(param):

    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
