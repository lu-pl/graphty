"""Tests for nested callable discriminated unions.

Covers:
- Mixed callable and string discriminated unions with heavy nesting.
"""

from typing import Annotated, Any, Literal

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Discriminator, Field, Tag
from tests.materializer.param import Expected, Parameter


class Cat(BaseModel):
    kind: Literal["cat"]
    name: str
    lives: int


class Dog(BaseModel):
    kind: Literal["dog"]
    name: str
    bark_volume: int


class Lizard(BaseModel):
    kind: Literal["lizard"]
    name: str
    length_cm: float


class Snake(BaseModel):
    kind: Literal["snake"]
    name: str
    venomous: bool


class Car(BaseModel):
    kind: Literal["car"]
    make: str
    doors: int


class Bike(BaseModel):
    kind: Literal["bike"]
    brand: str
    gears: int


def get_domain(v: Any) -> str | None:
    kind = v.get("kind") if isinstance(v, dict) else getattr(v, "kind", None)
    if kind in {"cat", "dog", "lizard", "snake"}:
        return "animal"
    if kind in {"car", "bike"}:
        return "vehicle"
    return None


def get_animal_group(v: Any) -> str | None:
    kind = v.get("kind") if isinstance(v, dict) else getattr(v, "kind", None)
    if kind in {"cat", "dog"}:
        return "mammal"
    if kind in {"lizard", "snake"}:
        return "reptile"
    return None


Mammal = Annotated[Cat | Dog, Field(discriminator="kind")]
Reptile = Annotated[Lizard | Snake, Field(discriminator="kind")]

Animal = Annotated[
    Annotated[Mammal, Tag("mammal")] | Annotated[Reptile, Tag("reptile")],
    Discriminator(get_animal_group),
]

Vehicle = Annotated[Car | Bike, Field(discriminator="kind")]

Thing = Annotated[
    Annotated[Animal, Tag("animal")] | Annotated[Vehicle, Tag("vehicle")],
    Discriminator(get_domain),
]


class Model(BaseModel):
    thing: Thing


class GroupedThing(BaseModel):
    model_config = ConfigDict(group_by="group_key")

    group_key: int
    thing: list[Thing]


class NestedGroupedThing(BaseModel):
    model_config = ConfigDict(group_by="group_key")
    group_key: int

    nested: list[GroupedThing]


data = {
    "kind": ["cat", "dog", "lizard", "snake", "car", "bike"],
    "name": ["Misty", "Rex", "Lizzy", "Snek", None, None],
    "lives": [9, None, None, None, None, None],
    "bark_volume": [None, 11, None, None, None, None],
    "length_cm": [None, None, 42.5, None, None, None],
    "venomous": [None, None, None, True, None, None],
    "make": [None, None, None, None, "Toyota", None],
    "doors": [None, None, None, None, 4, None],
    "brand": [None, None, None, None, None, "Trek"],
    "gears": [None, None, None, None, None, 21],
}

aggregation_data = {
    "group_key": [1, 1, 2, 2, 2, 1],  # cross Animal/Vehicle barrier twice
    "kind": ["cat", "dog", "lizard", "snake", "car", "bike"],
    "name": ["Misty", "Rex", "Lizzy", "Snek", None, None],
    "lives": [9, None, None, None, None, None],
    "bark_volume": [None, 11, None, None, None, None],
    "length_cm": [None, None, 42.5, None, None, None],
    "venomous": [None, None, None, True, None, None],
    "make": [None, None, None, None, "Toyota", None],
    "doors": [None, None, None, None, 4, None],
    "brand": [None, None, None, None, None, "Trek"],
    "gears": [None, None, None, None, None, 21],
}


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model, "data": data},
        expected=Expected(
            bindings=[
                {
                    "thing": {
                        "kind": "cat",
                        "name": "Misty",
                        "lives": 9,
                        "bark_volume": None,
                        "length_cm": None,
                        "venomous": None,
                        "make": None,
                        "doors": None,
                        "brand": None,
                        "gears": None,
                    }
                },
                {
                    "thing": {
                        "kind": "dog",
                        "name": "Rex",
                        "lives": None,
                        "bark_volume": 11,
                        "length_cm": None,
                        "venomous": None,
                        "make": None,
                        "doors": None,
                        "brand": None,
                        "gears": None,
                    }
                },
                {
                    "thing": {
                        "kind": "lizard",
                        "name": "Lizzy",
                        "lives": None,
                        "bark_volume": None,
                        "length_cm": 42.5,
                        "venomous": None,
                        "make": None,
                        "doors": None,
                        "brand": None,
                        "gears": None,
                    }
                },
                {
                    "thing": {
                        "kind": "snake",
                        "name": "Snek",
                        "lives": None,
                        "bark_volume": None,
                        "length_cm": None,
                        "venomous": True,
                        "make": None,
                        "doors": None,
                        "brand": None,
                        "gears": None,
                    }
                },
                {
                    "thing": {
                        "kind": "car",
                        "name": None,
                        "lives": None,
                        "bark_volume": None,
                        "length_cm": None,
                        "venomous": None,
                        "make": "Toyota",
                        "doors": 4,
                        "brand": None,
                        "gears": None,
                    }
                },
                {
                    "thing": {
                        "kind": "bike",
                        "name": None,
                        "lives": None,
                        "bark_volume": None,
                        "length_cm": None,
                        "venomous": None,
                        "make": None,
                        "doors": None,
                        "brand": "Trek",
                        "gears": 21,
                    }
                },
            ],
            model_dump=[
                {"thing": {"kind": "cat", "lives": 9, "name": "Misty"}},
                {"thing": {"bark_volume": 11, "kind": "dog", "name": "Rex"}},
                {"thing": {"kind": "lizard", "length_cm": 42.5, "name": "Lizzy"}},
                {"thing": {"kind": "snake", "name": "Snek", "venomous": True}},
                {"thing": {"doors": 4, "kind": "car", "make": "Toyota"}},
                {"thing": {"brand": "Trek", "gears": 21, "kind": "bike"}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": GroupedThing, "data": aggregation_data},
        expected=Expected(
            bindings=[
                {
                    "group_key": 1,
                    "thing": [
                        {
                            "name": "Misty",
                            "kind": "cat",
                            "length_cm": None,
                            "venomous": None,
                            "bark_volume": None,
                            "lives": 9,
                            "brand": None,
                            "gears": None,
                            "make": None,
                            "doors": None,
                        },
                        {
                            "name": "Rex",
                            "kind": "dog",
                            "length_cm": None,
                            "venomous": None,
                            "bark_volume": 11,
                            "lives": None,
                            "brand": None,
                            "gears": None,
                            "make": None,
                            "doors": None,
                        },
                        {
                            "name": None,
                            "kind": "bike",
                            "length_cm": None,
                            "venomous": None,
                            "bark_volume": None,
                            "lives": None,
                            "brand": "Trek",
                            "gears": 21,
                            "make": None,
                            "doors": None,
                        },
                    ],
                },
                {
                    "group_key": 2,
                    "thing": [
                        {
                            "name": "Lizzy",
                            "kind": "lizard",
                            "length_cm": 42.5,
                            "venomous": None,
                            "bark_volume": None,
                            "lives": None,
                            "brand": None,
                            "gears": None,
                            "make": None,
                            "doors": None,
                        },
                        {
                            "name": "Snek",
                            "kind": "snake",
                            "length_cm": None,
                            "venomous": True,
                            "bark_volume": None,
                            "lives": None,
                            "brand": None,
                            "gears": None,
                            "make": None,
                            "doors": None,
                        },
                        {
                            "name": None,
                            "kind": "car",
                            "length_cm": None,
                            "venomous": None,
                            "bark_volume": None,
                            "lives": None,
                            "brand": None,
                            "gears": None,
                            "make": "Toyota",
                            "doors": 4,
                        },
                    ],
                },
            ],
            model_dump=[
                {
                    "group_key": 1,
                    "thing": [
                        {"kind": "cat", "name": "Misty", "lives": 9},
                        {"kind": "dog", "name": "Rex", "bark_volume": 11},
                        {"kind": "bike", "brand": "Trek", "gears": 21},
                    ],
                },
                {
                    "group_key": 2,
                    "thing": [
                        {"kind": "lizard", "name": "Lizzy", "length_cm": 42.5},
                        {"kind": "snake", "name": "Snek", "venomous": True},
                        {"kind": "car", "make": "Toyota", "doors": 4},
                    ],
                },
            ],
        ),
    ),
    Parameter(
        kwargs={"model": NestedGroupedThing, "data": aggregation_data},
        expected=Expected(
            bindings=[
                {
                    "group_key": 1,
                    "nested": [
                        {
                            "group_key": 1,
                            "thing": [
                                {
                                    "name": "Misty",
                                    "kind": "cat",
                                    "length_cm": None,
                                    "venomous": None,
                                    "bark_volume": None,
                                    "lives": 9,
                                    "brand": None,
                                    "gears": None,
                                    "make": None,
                                    "doors": None,
                                },
                                {
                                    "name": "Rex",
                                    "kind": "dog",
                                    "length_cm": None,
                                    "venomous": None,
                                    "bark_volume": 11,
                                    "lives": None,
                                    "brand": None,
                                    "gears": None,
                                    "make": None,
                                    "doors": None,
                                },
                                {
                                    "name": None,
                                    "kind": "bike",
                                    "length_cm": None,
                                    "venomous": None,
                                    "bark_volume": None,
                                    "lives": None,
                                    "brand": "Trek",
                                    "gears": 21,
                                    "make": None,
                                    "doors": None,
                                },
                            ],
                        }
                    ],
                },
                {
                    "group_key": 2,
                    "nested": [
                        {
                            "group_key": 2,
                            "thing": [
                                {
                                    "name": "Lizzy",
                                    "kind": "lizard",
                                    "length_cm": 42.5,
                                    "venomous": None,
                                    "bark_volume": None,
                                    "lives": None,
                                    "brand": None,
                                    "gears": None,
                                    "make": None,
                                    "doors": None,
                                },
                                {
                                    "name": "Snek",
                                    "kind": "snake",
                                    "length_cm": None,
                                    "venomous": True,
                                    "bark_volume": None,
                                    "lives": None,
                                    "brand": None,
                                    "gears": None,
                                    "make": None,
                                    "doors": None,
                                },
                                {
                                    "name": None,
                                    "kind": "car",
                                    "length_cm": None,
                                    "venomous": None,
                                    "bark_volume": None,
                                    "lives": None,
                                    "brand": None,
                                    "gears": None,
                                    "make": "Toyota",
                                    "doors": 4,
                                },
                            ],
                        }
                    ],
                },
            ],
            model_dump=[
                {
                    "group_key": 1,
                    "nested": [
                        {
                            "group_key": 1,
                            "thing": [
                                {"kind": "cat", "name": "Misty", "lives": 9},
                                {"kind": "dog", "name": "Rex", "bark_volume": 11},
                                {"kind": "bike", "brand": "Trek", "gears": 21},
                            ],
                        }
                    ],
                },
                {
                    "group_key": 2,
                    "nested": [
                        {
                            "group_key": 2,
                            "thing": [
                                {"kind": "lizard", "name": "Lizzy", "length_cm": 42.5},
                                {"kind": "snake", "name": "Snek", "venomous": True},
                                {"kind": "car", "make": "Toyota", "doors": 4},
                            ],
                        }
                    ],
                },
            ],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_nested_callable_discriminated_union(param):
    materializer = ModelMaterializer(**param.kwargs)
    assert list(materializer.generate_bindings()) == param.expected.bindings
    assert [
        m.model_dump() for m in materializer.generate_models()
    ] == param.expected.model_dump


def test_nested_callable_discriminated_union_model_types():
    cat, dog, lizard, snake, car, bike = ModelMaterializer(
        model=Model, data=data
    ).generate_models()
    assert isinstance(cat.thing, Cat)
    assert isinstance(dog.thing, Dog)
    assert isinstance(lizard.thing, Lizard)
    assert isinstance(snake.thing, Snake)
    assert isinstance(car.thing, Car)
    assert isinstance(bike.thing, Bike)
