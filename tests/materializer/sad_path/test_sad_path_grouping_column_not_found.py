"""Sad path tests for grouping keys that resolve to columns absent from the data (#125)."""

import re
from typing import Literal, NamedTuple

import pytest
from graphty import ConfigDict, GroupByColumnNotFoundError, ModelMaterializer
from pydantic import AliasChoices, BaseModel, Field

data: list[dict[str, object]] = [
    {"name": "Ada", "kind": "a", "other": 1},
    {"name": "Alan", "kind": "a", "other": 2},
]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="key")

    key: str = "default"
    name: list[str]


class Model2(BaseModel):
    model_config = ConfigDict(group_by="key")

    key: str = Field(default="default", validation_alias="k")
    name: list[str]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="key")

    key: str = Field(default="default", validation_alias=AliasChoices("k", "kk"))
    name: list[str]


class Model4(BaseModel):
    other: int
    child: Model1


class Model5(BaseModel):
    model_config = ConfigDict(group_by="key")

    kind: Literal["a"]
    key: str = "default"
    name: list[str]


class Model6(BaseModel):
    kind: Literal["b"]


class Model7(BaseModel):
    other: int
    member: Model5 | Model6 = Field(discriminator="kind")


class Model8(BaseModel):
    model_config = ConfigDict(
        group_by="key", validate_by_name=True, validate_by_alias=False
    )

    key: str = Field(default="default", validation_alias="k")
    name: list[str]


class Parameter(NamedTuple):
    model: type[BaseModel]
    match: str
    comment: str = ""


def message(model: str, group_by_column: str) -> str:
    return re.escape(
        f"Grouping key 'key' for '{model}' "
        "does not reference a column in the data projection. "
        f"Expected column '{group_by_column}' (alias-resolved); "
        "available columns: ['kind', 'name', 'other']."
    )


params: list[Parameter] = [
    Parameter(
        model=Model1,
        match=message(model="Model1", group_by_column="key"),
        comment="Plain grouping key without alias.",
    ),
    Parameter(
        model=Model2,
        match=message(model="Model2", group_by_column="k"),
        comment="Grouping key with a single validation alias.",
    ),
    Parameter(
        model=Model3,
        match=message(model="Model3", group_by_column="k"),
        comment="Unresolvable AliasChoices fall back to the first choice (#124).",
    ),
    Parameter(
        model=Model4,
        match=message(model="Model1", group_by_column="key"),
        comment="Grouping key of a nested model.",
    ),
    Parameter(
        model=Model7,
        match=message(model="Model5", group_by_column="key"),
        comment="Grouping key of a discriminated union member.",
    ),
    Parameter(
        model=Model8,
        match=message(model="Model8", group_by_column="key"),
        comment="With validate_by_alias=False, Pydantic ignores the declared alias.",
    ),
]


@pytest.mark.parametrize("param", params)
def test_sad_path_grouping_column_not_found(param: Parameter) -> None:
    materializer = ModelMaterializer(model=param.model, data=data)

    with pytest.raises(GroupByColumnNotFoundError, match=param.match):
        list(materializer.generate_bindings())
