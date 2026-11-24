from dataclasses import dataclass
from typing import Annotated, Any, Literal

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import AliasChoices, BaseModel, Discriminator, Field, Tag

data = [
    {"a": 1},
    {"a": 2},
    {"a": 3},
]


class Model1(BaseModel):
    a: int
    b: int = 1
    c: int = Field(default_factory=lambda: 2)
    d: int = Field(default_factory=lambda data: 3)


class Model2(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: int = 1
    c: int = Field(default_factory=lambda: 2)
    d: int = Field(default_factory=lambda data: 3)


class Model3(BaseModel):
    nested: Model1


class Model4(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model1


class Model5(BaseModel):
    nested: Model2


class Model6(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model2


class Model7(BaseModel):
    x: int = 1


class Model8(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: list[int] = []
    c: list[int] = Field(default_factory=lambda: [1])
    d: list[int] = Field(default_factory=lambda data: [data["a"]])
    e: list[int] = Field(default=[], alias="x")


class Model9(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: list[int] = []
    c: list[int]


class Model10(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: list[Model8]


class Model11(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    nested: Model8


class Model12(BaseModel):
    a: int
    b: int = Field(default=0, validation_alias="bee")


class Model13(BaseModel):
    a: int
    b: int = Field(default=0, validation_alias=AliasChoices("b", "bee"))


class Model14(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    a: int
    b: int = Field(default=0, validation_alias="bee")


class Model15(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    b: list[int] = Field(default=[], validation_alias=AliasChoices("b", "bee"))


class Cat(BaseModel):
    pet_type: Literal["cat"]
    name: str = "unnamed"


class Dog(BaseModel):
    pet_type: Literal["dog"]
    good_boy: bool = Field(default=True, validation_alias="good")


class Model16(BaseModel):
    pet: Cat | Dog = Field(discriminator="pet_type")


class Model17(BaseModel):
    model_config = ConfigDict(group_by="a")

    a: int
    pets: list[Annotated[Cat | Dog, Field(discriminator="pet_type")]]


def get_pet_type(v: Any) -> str | None:
    if isinstance(v, dict):
        return v.get("pet_type")
    return getattr(v, "pet_type", None)


class Model18(BaseModel):
    pet: Annotated[
        Annotated[Cat, Tag("cat")] | Annotated[Dog, Tag("dog")],
        Discriminator(get_pet_type),
    ]


class Model19(BaseModel):
    x: int = 1


class Model20(BaseModel):
    y: int = 2


class Model21(BaseModel):
    a: int
    nested: Annotated[
        Annotated[Model19, Tag("x")] | Annotated[Model20, Tag("y")],
        Discriminator(lambda data: "x"),
    ]


class SaltwaterFish(BaseModel):
    pet_type: Literal["fish"]
    water: Literal["salt"]
    fins: int = 2


class FreshwaterFish(BaseModel):
    pet_type: Literal["fish"]
    water: Literal["fresh"]


Fish = Annotated[SaltwaterFish | FreshwaterFish, Field(discriminator="water")]


class Model22(BaseModel):
    pet: Annotated[Fish | Dog, Field(discriminator="pet_type")]


union_data = [
    {"pet_type": "cat"},
    {"pet_type": "dog"},
]

nested_union_data = [
    {"pet_type": "fish", "water": "salt"},
    {"pet_type": "fish", "water": "fresh"},
    {"pet_type": "dog", "water": None},
]

grouped_data = [
    {"a": 1},
    {"a": 1},
    {"a": 2},
    {"a": 3},
]


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
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ]
        ),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": 1, "c": 2, "d": 3},
                {"a": 2, "b": 1, "c": 2, "d": 3},
                {"a": 3, "b": 1, "c": 2, "d": 3},
            ]
        ),
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=snapshot(
            [{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}]
        ),
        model_dump=snapshot(
            [
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=snapshot(
            [{"nested": {"a": 1}}, {"nested": {"a": 2}}, {"nested": {"a": 3}}]
        ),
        model_dump=snapshot(
            [
                {"nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(
        model=Model6,
        data=data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": 1, "c": 2, "d": 3}},
                {"a": 2, "nested": {"a": 2, "b": 1, "c": 2, "d": 3}},
                {"a": 3, "nested": {"a": 3, "b": 1, "c": 2, "d": 3}},
            ]
        ),
    ),
    Parameter(model=Model7, data=[], bindings=snapshot([]), model_dump=snapshot([])),
    # list-of-scalar fields with defaults and no column in the data (#106)
    Parameter(
        model=Model8,
        data=grouped_data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot(
            [
                {"a": 1, "b": [], "c": [1], "d": [1], "e": []},
                {"a": 2, "b": [], "c": [1], "d": [2], "e": []},
                {"a": 3, "b": [], "c": [1], "d": [3], "e": []},
            ]
        ),
    ),
    Parameter(
        model=Model9,
        data=[{"a": 1, "c": 1}, {"a": 1, "c": 2}, {"a": 2, "c": 3}],
        bindings=snapshot([{"a": 1, "c": [1, 2]}, {"a": 2, "c": [3]}]),
        model_dump=snapshot(
            [{"a": 1, "b": [], "c": [1, 2]}, {"a": 2, "b": [], "c": [3]}]
        ),
    ),
    Parameter(
        model=Model10,
        data=grouped_data,
        bindings=snapshot(
            [
                {"a": 1, "nested": [{"a": 1}]},
                {"a": 2, "nested": [{"a": 2}]},
                {"a": 3, "nested": [{"a": 3}]},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": [{"a": 1, "b": [], "c": [1], "d": [1], "e": []}]},
                {"a": 2, "nested": [{"a": 2, "b": [], "c": [1], "d": [2], "e": []}]},
                {"a": 3, "nested": [{"a": 3, "b": [], "c": [1], "d": [3], "e": []}]},
            ]
        ),
    ),
    Parameter(
        model=Model11,
        data=grouped_data,
        bindings=snapshot(
            [
                {"a": 1, "nested": {"a": 1}},
                {"a": 2, "nested": {"a": 2}},
                {"a": 3, "nested": {"a": 3}},
            ]
        ),
        model_dump=snapshot(
            [
                {"a": 1, "nested": {"a": 1, "b": [], "c": [1], "d": [1], "e": []}},
                {"a": 2, "nested": {"a": 2, "b": [], "c": [1], "d": [2], "e": []}},
                {"a": 3, "nested": {"a": 3, "b": [], "c": [1], "d": [3], "e": []}},
            ]
        ),
    ),
    # aliased fields with defaults and no matching column in the data (#107)
    Parameter(
        model=Model12,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot([{"a": 1, "b": 0}, {"a": 2, "b": 0}, {"a": 3, "b": 0}]),
    ),
    Parameter(
        model=Model13,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot([{"a": 1, "b": 0}, {"a": 2, "b": 0}, {"a": 3, "b": 0}]),
    ),
    Parameter(
        model=Model14,
        data=data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot([{"a": 1, "b": 0}, {"a": 2, "b": 0}, {"a": 3, "b": 0}]),
    ),
    Parameter(
        model=Model15,
        data=grouped_data,
        bindings=snapshot([{"a": 1}, {"a": 2}, {"a": 3}]),
        model_dump=snapshot([{"a": 1, "b": []}, {"a": 2, "b": []}, {"a": 3, "b": []}]),
    ),
    # model union members with defaults and no matching column in the data (#105)
    Parameter(
        model=Model16,
        data=union_data,
        bindings=snapshot([{"pet": {"pet_type": "cat"}}, {"pet": {"pet_type": "dog"}}]),
        model_dump=snapshot(
            [
                {"pet": {"pet_type": "cat", "name": "unnamed"}},
                {"pet": {"pet_type": "dog", "good_boy": True}},
            ]
        ),
    ),
    Parameter(
        model=Model17,
        data=[{"a": 1, "pet_type": "cat"}, {"a": 1, "pet_type": "dog"}],
        bindings=snapshot(
            [{"a": 1, "pets": [{"pet_type": "cat"}, {"pet_type": "dog"}]}]
        ),
        model_dump=snapshot(
            [
                {
                    "a": 1,
                    "pets": [
                        {"pet_type": "cat", "name": "unnamed"},
                        {"pet_type": "dog", "good_boy": True},
                    ],
                }
            ]
        ),
    ),
    Parameter(
        model=Model18,
        data=union_data,
        bindings=snapshot([{"pet": {"pet_type": "cat"}}, {"pet": {"pet_type": "dog"}}]),
        model_dump=snapshot(
            [
                {"pet": {"pet_type": "cat", "name": "unnamed"}},
                {"pet": {"pet_type": "dog", "good_boy": True}},
            ]
        ),
    ),
    Parameter(
        model=Model21,
        data=[{"a": 1}],
        bindings=snapshot([{"a": 1, "nested": {"a": 1}}]),
        model_dump=snapshot([{"a": 1, "nested": {"x": 1}}]),
    ),
    Parameter(
        model=Model22,
        data=nested_union_data,
        bindings=snapshot(
            [
                {"pet": {"water": "salt", "pet_type": "fish"}},
                {"pet": {"water": "fresh", "pet_type": "fish"}},
                {"pet": {"water": None, "pet_type": "dog"}},
            ]
        ),
        model_dump=snapshot(
            [
                {"pet": {"pet_type": "fish", "water": "salt", "fins": 2}},
                {"pet": {"pet_type": "fish", "water": "fresh"}},
                {"pet": {"pet_type": "dog", "good_boy": True}},
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materializer_default_values(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
