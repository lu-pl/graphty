from typing import Annotated, Any, Literal

from graphty.planner import LazyFramePlanner
from pydantic import BaseModel, Discriminator, Field, Tag


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


Mammal = Annotated[
    Cat | Dog,
    Field(discriminator="kind"),
]

Reptile = Annotated[
    Lizard | Snake,
    Field(discriminator="kind"),
]

Animal = Annotated[
    Annotated[Mammal, Tag("mammal")] | Annotated[Reptile, Tag("reptile")],
    Discriminator(get_animal_group),
]

Vehicle = Annotated[
    Car | Bike,
    Field(discriminator="kind"),
]

Thing = Annotated[
    Annotated[Animal, Tag("animal")] | Annotated[Vehicle, Tag("vehicle")],
    Discriminator(get_domain),
]


class Model(BaseModel):
    thing: Thing


EXPECTED = [
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
        },
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
        },
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
        },
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
        },
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
        },
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
        },
    },
]


def test_planner_callable_discriminated_union():
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

    planner = LazyFramePlanner(model=Model, data=data)
    frame = planner.run().collect()

    dicts = frame.to_dicts()
    assert dicts == EXPECTED

    for binding in dicts:
        assert Model.model_validate(binding)
