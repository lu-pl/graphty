"""Tests for unresolvable AliasChoices with the field name present as a column (#117)."""

from typing import NamedTuple

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, Field

data: list[dict[str, object]] = [
    {"name": "Ada", "nickname": "wrong", "age": 36},
    {"name": "Ada", "nickname": "wrong", "age": 36},
    {"name": "Alan", "nickname": "wrong", "age": 41},
]


class Model1(BaseModel):
    name: str
    nickname: str = Field(
        default="default", validation_alias=AliasChoices("nick", "alias")
    )


class Model2(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    nickname: str = Field(
        default="default", validation_alias=AliasChoices("nick", "alias")
    )


class Model3(BaseModel):
    model_config = ConfigDict(group_by="name")

    name: str
    nickname: list[int] = Field(
        default=[], validation_alias=AliasChoices("nick", "alias")
    )


class Parameter(NamedTuple):
    model: type[BaseModel]
    bindings: list[dict[str, object]]
    model_dump: list[dict[str, object]]
    comment: str = ""


params: list[Parameter] = [
    Parameter(
        model=Model1,
        bindings=snapshot([{"name": "Ada"}, {"name": "Ada"}, {"name": "Alan"}]),
        model_dump=snapshot(
            [
                {"name": "Ada", "nickname": "default"},
                {"name": "Ada", "nickname": "default"},
                {"name": "Alan", "nickname": "default"},
            ]
        ),
        comment="The field name column must not leak into the bindings.",
    ),
    Parameter(
        model=Model2,
        bindings=snapshot([{"name": "Ada"}, {"name": "Ada"}, {"name": "Alan"}]),
        model_dump=snapshot(
            [
                {"name": "Ada", "nickname": "default"},
                {"name": "Ada", "nickname": "default"},
                {"name": "Alan", "nickname": "default"},
            ]
        ),
        comment="A leaked field name column would fail with extra_forbidden.",
    ),
    Parameter(
        model=Model3,
        bindings=snapshot([{"name": "Ada"}, {"name": "Alan"}]),
        model_dump=snapshot(
            [{"name": "Ada", "nickname": []}, {"name": "Alan", "nickname": []}]
        ),
        comment="The field name column must not be collected for list fields.",
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_alias_choices_fallback(param: Parameter) -> None:
    materializer = ModelMaterializer(model=param.model, data=data)

    bindings: list[dict[str, object]] = list(materializer.generate_bindings())
    model_dump: list[dict[str, object]] = [
        model.model_dump() for model in materializer.generate_models()
    ]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
