"""Tests for mixed string/callable discriminated unions with a simple model union member.

Covers:
- String discriminated union where one member is a simple model
  and another points to a nested callable discriminated union.
  This is the inverse test to test_callable_string_mixed_discrimination.py.
- Discrimnated union model aggregation (top-level + nested union aggregation)
"""

from dataclasses import dataclass
from typing import Annotated, Any, Literal

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Discriminator, Field, Tag


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


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params = [
    Parameter(
        model=Model,
        data=data,
        bindings=snapshot(
            [
                {"thing": {"kind": "cat", "bike_type": None, "name": "Muzi"}},
                {"thing": {"kind": "bike", "bike_type": "road", "name": None}},
                {"thing": {"kind": "bike", "bike_type": "mountain", "name": None}},
            ]
        ),
        model_dump=snapshot(
            [
                {"thing": {"kind": "cat", "name": "Muzi"}},
                {"thing": {"kind": "bike", "bike_type": "road"}},
                {"thing": {"kind": "bike", "bike_type": "mountain"}},
            ]
        ),
    ),
    Parameter(
        model=GroupedThing,
        data=data,
        bindings=snapshot(
            [
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
            ]
        ),
        model_dump=snapshot(
            [
                {"kind": "cat", "nested": [{"kind": "cat", "name": "Muzi"}]},
                {
                    "kind": "bike",
                    "nested": [
                        {"kind": "bike", "bike_type": "road"},
                        {"kind": "bike", "bike_type": "mountain"},
                    ],
                },
            ]
        ),
    ),
    Parameter(
        model=NestedGroupedThing,
        data=data,
        bindings=snapshot(
            [
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
            ]
        ),
        model_dump=snapshot(
            [
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
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_string_callable_mixed_discrimination(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)
    assert list(materializer.generate_bindings()) == param.bindings
    assert [m.model_dump() for m in materializer.generate_models()] == param.model_dump


def test_string_callable_mixed_discrimination_model_types():
    cat, road_bike, mountain_bike = ModelMaterializer(
        model=Model, data=data
    ).generate_models()
    assert isinstance(cat.thing, Cat)
    assert isinstance(road_bike.thing, RoadBike)
    assert isinstance(mountain_bike.thing, MountainBike)
