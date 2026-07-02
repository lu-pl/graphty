"""Basic planner tests."""

import json
import logging
from typing import NamedTuple

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Field
from tests.materializer.param import Expected, Parameter


class TestParameter(NamedTuple):
    kwargs: dict
    expected: list[dict]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int = Field(exclude=True)
    y: int


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: int


data = [{"x": 1, "y": 2}, {"x": 1, "y": 2}]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(bindings=[{"x": 1, "y": 2}], model_dump=[{"y": 2}]),
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


@pytest.mark.parametrize("param", params)
def test_materalizer_logging(param, caplog):
    """Check the structured logging message from ModelMaterializer at level=logging.DEBUG.

    The test uses the caplog fixture to introspect the log structured message
    and parses the JSON part of the message to compare it to the current `binding` parameter.
    """

    with caplog.at_level(logging.DEBUG):
        materializer = ModelMaterializer(**param.kwargs)

        for _, binding_from_param in zip(
            materializer.generate_models(),
            param.expected.bindings,
        ):
            *_, json_part = caplog.text.rpartition(" >>> ")
            binding_from_json = json.loads(json_part)["binding"]

            assert binding_from_json == binding_from_param
