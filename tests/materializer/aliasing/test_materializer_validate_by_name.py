"""Tests for alias resolution order under validate_by_name=True."""

from typing import NamedTuple

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, Field

data: list[dict[str, object]] = [
    {"x": 1, "a": 10, "b": 100, "y": 1},
    {"x": 2, "a": 10, "b": 100, "y": 2},
]


class Model1(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    x: int = Field(validation_alias="a")


class Model2(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    x: int = Field(validation_alias=AliasChoices("a", "b"))


class Model3(BaseModel):
    model_config = ConfigDict(
        validate_by_alias=True, validate_by_name=True, group_by="x"
    )

    x: int = Field(validation_alias="a")
    y: list[int]


class Parameter(NamedTuple):
    model: type[BaseModel]
    bindings: list[dict[str, object]]
    model_dump: list[dict[str, object]]
    comment: str = ""


params: list[Parameter] = [
    Parameter(
        model=Model1,
        bindings=snapshot([{"a": 10}, {"a": 10}]),
        model_dump=snapshot([{"x": 10}, {"x": 10}]),
        comment="A present alias takes precedence over the field name.",
    ),
    Parameter(
        model=Model2,
        bindings=snapshot([{"a": 10}, {"a": 10}]),
        model_dump=snapshot([{"x": 10}, {"x": 10}]),
        comment="A present alias choice takes precedence over the field name.",
    ),
    Parameter(
        model=Model3,
        bindings=snapshot([{"a": 10, "y": [1, 2]}]),
        model_dump=snapshot([{"x": 10, "y": [1, 2]}]),
        comment="Grouping uses the alias column, not the field name column.",
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_validate_by_name(param: Parameter) -> None:
    materializer = ModelMaterializer(model=param.model, data=data)

    bindings: list[dict[str, object]] = list(materializer.generate_bindings())
    model_dump: list[dict[str, object]] = [
        model.model_dump() for model in materializer.generate_models()
    ]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
