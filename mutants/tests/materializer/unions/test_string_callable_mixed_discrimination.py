"""Tests for mixed string/callable discriminated unions with a simple model union member.

Covers:
- String discriminated union where one member is a simple model
  and another points to a nested callable discriminated union.
  This is the inverse test to test_callable_string_mixed_discrimination.py.
- Discrimnated union model aggregation (top-level + nested union aggregation)
"""

from typing import Annotated, Any, Literal

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Discriminator, Field, Tag
from tests.materializer.param import Expected, Parameter


class Cat(BaseModel):
    kind: Literal["cat"]
    name: str


class RoadBike(BaseModel):
    kind: Literal["bike"]
    bike_type: Literal["road"]


class MountainBike(BaseModel):
    kind: Literal["bike"]
    bike_type: Literal["mountain"]


def get_bike_type(v: Any) -> str | None:
    bike_type = (
        v.get("bike_type") if isinstance(v, dict) else getattr(v, "bike_type", None)
    )
    if bike_type == "road":
        return "road"
    if bike_type == "mountain":
        return "mountain"


Bike = Annotated[
    Annotated[RoadBike, Tag("road")] | Annotated[MountainBike, Tag("mountain")],
    Discriminator(get_bike_type),
]

Thing = Annotated[Bike | Cat, Field(discriminator="kind")]


class Model(BaseModel):
    thing: Thing


class GroupedThing(BaseModel):
    model_config = ConfigDict(group_by="kind")

    kind: str
    nested: list[Thing]


class NestedGroupedThing(BaseModel):
    model_config = ConfigDict(group_by="kind")

    kind: str
    nested: list[GroupedThing]


data = [
    {"kind": "cat", "name": "Muzi", "bike_type": None},
    {"kind": "bike", "name": None, "bike_type": "road"},
    {"kind": "bike", "name": None, "bike_type": "mountain"},
]


params = [
    Parameter(
        kwargs={"model": Model, "data": data},
        expected=Expected(
            bindings=[
                {"thing": {"kind": "cat", "bike_type": None, "name": "Muzi"}},
                {"thing": {"kind": "bike", "bike_type": "road", "name": None}},
                {"thing": {"kind": "bike", "bike_type": "mountain", "name": None}},
            ],
            model_dump=[
                {"thing": {"kind": "cat", "name": "Muzi"}},
                {"thing": {"kind": "bike", "bike_type": "road"}},
                {"thing": {"kind": "bike", "bike_type": "mountain"}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": GroupedThing, "data": data},
        expected=Expected(
            bindings=[
                {
                    "kind": "cat",
                    "nested": [{"kind": "cat", "bike_type": None, "name": "Muzi"}],
                },
                {
                    "kind": "bike",
                    "nested": [
                        {"kind": "bike", "bike_type": "road", "name": None},
                        {"kind": "bike", "bike_type": "mountain", "name": None},
                    ],
                },
            ],
            model_dump=[
                {"kind": "cat", "nested": [{"kind": "cat", "name": "Muzi"}]},
                {
                    "kind": "bike",
                    "nested": [
                        {"kind": "bike", "bike_type": "road"},
                        {"kind": "bike", "bike_type": "mountain"},
                    ],
                },
            ],
        ),
    ),
    Parameter(
        kwargs={"model": NestedGroupedThing, "data": data},
        expected=Expected(
            bindings=[
                {
                    "kind": "cat",
                    "nested": [
                        {
                            "kind": "cat",
                            "nested": [
                                {"kind": "cat", "bike_type": None, "name": "Muzi"}
                            ],
                        }
                    ],
                },
                {
                    "kind": "bike",
                    "nested": [
                        {
                            "kind": "bike",
                            "nested": [
                                {"kind": "bike", "bike_type": "road", "name": None},
                                {"kind": "bike", "bike_type": "mountain", "name": None},
                            ],
                        }
                    ],
                },
            ],
            model_dump=[
                {
                    "kind": "cat",
                    "nested": [
                        {"kind": "cat", "nested": [{"kind": "cat", "name": "Muzi"}]}
                    ],
                },
                {
                    "kind": "bike",
                    "nested": [
                        {
                            "kind": "bike",
                            "nested": [
                                {"kind": "bike", "bike_type": "road"},
                                {"kind": "bike", "bike_type": "mountain"},
                            ],
                        }
                    ],
                },
            ],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_string_callable_mixed_discrimination(param):
    materializer = ModelMaterializer(**param.kwargs)
    assert list(materializer.generate_bindings()) == param.expected.bindings
    assert [
        m.model_dump() for m in materializer.generate_models()
    ] == param.expected.model_dump


def test_string_callable_mixed_discrimination_model_types():
    cat, road_bike, mountain_bike = ModelMaterializer(
        model=Model, data=data
    ).generate_models()
    assert isinstance(cat.thing, Cat)
    assert isinstance(road_bike.thing, RoadBike)
    assert isinstance(mountain_bike.thing, MountainBike)
