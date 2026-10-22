"""Basic planner tests."""

import json
import logging
from dataclasses import dataclass

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Field


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int = Field(exclude=True)
    y: int


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: int


data = [{"x": 1, "y": 2}, {"x": 1, "y": 2}]


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
        bindings=snapshot([{"x": 1, "y": 2}]),
        model_dump=snapshot([{"y": 2}]),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot([{"x": 1, "y": 2}]),
        model_dump=snapshot([{"x": 1, "y": 2}]),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_basic(param, caplog):
    """Check materializer output and the structured DEBUG logging message it emits.

    The logging part reuses the already-verified `bindings` list (not the raw
    `param.bindings` snapshot) to introspect `caplog`'s structured message, since
    a single snapshot object can only be used in one access mode (here: `==`).
    """

    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump

    with caplog.at_level(logging.DEBUG):
        logging_materializer = ModelMaterializer(model=param.model, data=param.data)

        for _, binding_from_param in zip(
            logging_materializer.generate_models(),
            bindings,
        ):
            *_, json_part = caplog.text.rpartition(" >>> ")
            binding_from_json = json.loads(json_part)["binding"]

            assert binding_from_json == binding_from_param
