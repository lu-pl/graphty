from dataclasses import dataclass

import pytest
from graphty.utils.alias_map import AliasMap
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class Model1(BaseModel):
    model_config = ConfigDict(
        alias_generator=lambda v: "".join(v.capitalize() for v in v.split("_")),
        extra="forbid",
    )

    id1: int

    id2: int = Field(alias="user_id_2")
    id3: int = Field(alias="user_id_3", alias_priority=1)
    id4: int = Field(alias="user_id_4", alias_priority=2)

    id5: int = Field(validation_alias="user_id_5", alias_priority=1)
    id6: int = Field(validation_alias="user_id_6", alias_priority=2)

    display_name_1: str = Field(
        validation_alias=AliasChoices("displayName", "name", "label")
    )

    display_name_2: str = Field(
        validation_alias=AliasChoices("displayName", "name", "label"), alias_priority=1
    )
    display_name_3: str = Field(
        validation_alias=AliasChoices("displayName", "name", "label"), alias_priority=2
    )

    display_name_4: str = Field(validation_alias=AliasChoices("dne"), alias_priority=2)
    display_name_5: str = Field(
        validation_alias=AliasChoices("dne", "nope"),
        alias_priority=1,  # crashes with alias_priority=2
    )


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    b: int = Field(validation_alias="y")
    c: int = Field(
        validation_alias=AliasChoices(
            "a",
            "x",
        )
    )


class Model3(BaseModel):
    x: int = Field(
        alias="a",
        validation_alias="b",
        alias_priority=1,
    )
    y: int = Field(alias="a", validation_alias="b", alias_priority=2)
    z: int = Field(alias="a", validation_alias="b")


class Model4(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=False)

    my_field: str = Field(validation_alias="my_alias")


class Model5(BaseModel):
    model_config = ConfigDict(validate_by_alias=False, validate_by_name=True)

    my_field: str = Field(validation_alias="my_alias")


class Model6(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    my_field: str = Field(validation_alias="my_alias")


class Model7(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    my_field: str = Field(validation_alias="my_alias")


class Model8(BaseModel):
    x: int = Field(alias=AliasChoices("a"))


@dataclass
class Parameter:
    model: object
    projection: object
    expected: object


params: list[Parameter] = [
    # Full test case model with alias, validation alias, alias generator, alias
    # choice, and alias priority -- uses almost all functionality AliasMap
    # supports.
    Parameter(
        model=Model1,
        projection={"name"},
        expected=snapshot(
            {
                "id1": "Id1",
                "id2": "user_id_2",
                "id3": "Id3",
                "id4": "user_id_4",
                "id5": "Id5",
                "id6": "user_id_6",
                "display_name_1": "name",
                "display_name_2": "DisplayName2",
                "display_name_3": "name",
                "display_name_4": "dne",
                "display_name_5": "DisplayName5",
            }
        ),
    ),
    # Simple test model with validation_alias and AliasChoice.
    Parameter(
        model=Model2,
        projection={"a"},
        expected=snapshot({"x": "x", "b": "y", "c": "a"}),
    ),
    # Checks AliasMap resolution for fields with both alias and validation_alias
    # definitions and different alias_priority values set.
    Parameter(
        model=Model3,
        projection=set(),
        expected=snapshot({"x": "b", "y": "b", "z": "b"}),
    ),
    # Test cases for validate_by_alias/validate_by_name combinations.
    Parameter(
        model=Model4, projection=set(), expected=snapshot({"my_field": "my_alias"})
    ),
    Parameter(
        model=Model5, projection=set(), expected=snapshot({"my_field": "my_field"})
    ),
    Parameter(
        model=Model6,
        projection={"my_field"},
        expected=snapshot({"my_field": "my_field"}),
    ),
    Parameter(
        model=Model7,
        projection={"my_alias"},
        expected=snapshot({"my_field": "my_alias"}),
    ),
    # Single entry AliasChoice should behave like a regular alias parameter and
    # therefore is decidable regardless of the projection.
    Parameter(model=Model8, projection=set(), expected=snapshot({"x": "a"})),
]


@pytest.mark.parametrize("param", params)
def test_alias_map(param):
    alias_map = AliasMap(model=param.model, projection=param.projection)
    assert alias_map == param.expected
