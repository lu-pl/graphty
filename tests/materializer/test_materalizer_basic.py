"""Basic planner tests."""

from typing import NamedTuple

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


class TestParameter(NamedTuple):
    kwargs: dict
    expected: list[dict]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")
    y: int


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")
    x: int
    y: int


data = [{"x": 1, "y": 2}, {"x": 1, "y": 2}]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data}, expected=Expected(bindings=[{"y": 2}])
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(bindings=[{"x": 1, "y": 2}]),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_basic(param):

    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
