"""Cases for AliasMap tests."""

from typing import NamedTuple

from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class TestParameter(NamedTuple):
    kwargs: dict[str, object]
    expected: dict[str, str]
    description: str | None = None


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
  
  my_field: str = Field(validation_alias='my_alias')


class Model5(BaseModel):
  model_config = ConfigDict(validate_by_alias=False, validate_by_name=True)
  
  my_field: str = Field(validation_alias='my_alias')


class Model6(BaseModel):
  model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
  
  my_field: str = Field(validation_alias='my_alias')

class Model7(BaseModel):
  model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
  
  my_field: str = Field(validation_alias='my_alias')



params: list[TestParameter] = [
    TestParameter(
        description="""Full test case model with
        - alias
        - validation alias
        - alias generator
        - alias choice
        - alias priority

        This model uses almost all of the functionality supported by AliasMap.
        """,
        kwargs={
            "model": Model1,
            "projection": {"name"},
        },
        expected={
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
        },
    ),
    TestParameter(
        description="Simple test model with validation_alias and AliasChoice.",
        kwargs={"model": Model2, "projection": {"a"}},
        expected={"x": "x", "b": "y", "c": "a"},
    ),
    TestParameter(
        description="""Test case that checks AliasMap resolution
        for fields with both alias and validation_alias definitions
        and different alias_priority values set.""",
        kwargs={"model": Model3, "projection": set()},
        expected={"x": "b", "y": "b", "z": "b"},
    ),
    TestParameter(description="Test case for validate_by_alias/validate_by_name combinations.", kwargs={"model": Model4, "projection": set()}, expected={'my_field': 'my_alias'}),
    TestParameter(description="Test case for validate_by_alias/validate_by_name combinations.", kwargs={"model": Model5, "projection": set()}, expected={'my_field': 'my_field'}),
    TestParameter(description="Test case for validate_by_alias/validate_by_name combinations.", kwargs={"model": Model6, "projection": {"my_field"}}, expected={'my_field': 'my_field'}),
    TestParameter(description="Test case for validate_by_alias/validate_by_name combinations.", kwargs={"model": Model7, "projection": {"my_alias"}}, expected={'my_field': 'my_alias'}),
]
