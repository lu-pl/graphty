"""Sad path tests for unresolvable AliasChoices with the field name present as a column (#117)."""

import re
from typing import NamedTuple

import pytest
from graphty import ModelMaterializer
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, Field, ValidationError

data: list[dict[str, object]] = [
    {"name": "Ada", "nickname": "wrong", "age": 36},
    {"name": "Alan", "nickname": "wrong", "age": 41},
]


class Model1(BaseModel):
    name: str
    nickname: str = Field(validation_alias=AliasChoices("nick", "alias"))


class Parameter(NamedTuple):
    model: type[BaseModel]
    bindings: list[dict[str, object]]
    exception: type[Exception]
    match: str
    comment: str = ""


params: list[Parameter] = [
    Parameter(
        model=Model1,
        bindings=snapshot([{"name": "Ada"}, {"name": "Alan"}]),
        exception=ValidationError,
        match=re.escape(
            "nick\n  Field required "
            "[type=missing, input_value={'name': 'Ada'}, input_type=dict]"
        ),
        comment=(
            "Pydantic reports the missing field under the first choice; "
            "the field name column must not leak into the validation input."
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_sad_path_alias_choices_fallback(param: Parameter) -> None:
    materializer = ModelMaterializer(model=param.model, data=data)

    bindings: list[dict[str, object]] = list(materializer.generate_bindings())
    assert bindings == param.bindings

    with pytest.raises(param.exception, match=param.match):
        list(materializer.generate_models())
