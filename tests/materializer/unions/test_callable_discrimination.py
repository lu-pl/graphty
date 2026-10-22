"""Basic test for callable discriminated unions.

This is the example from the Pydantic docs section on callable discriminated unions;
see https://pydantic.dev/docs/validation/latest/concepts/unions/#discriminated-unions-with-callable-discriminator.

Covers:
- Basic two-member callable discriminated union
- Discrimnated union model aggregation (top-level + nested union aggregation)
"""

from dataclasses import dataclass
from typing import Annotated, Any, Literal, Optional, Union

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Discriminator, Field, Tag


class Pie(BaseModel):
    time_to_cook: int


class ApplePie(Pie):
    fruit: Literal["apple"] = "apple"


class PumpkinPie(Pie):
    filling: Literal["pumpkin"] = "pumpkin"


def get_discriminator_value(v: Any) -> Optional[str]:
    if isinstance(v, dict):
        return v.get("fruit") or v.get("filling")
    return getattr(v, "fruit", None) or getattr(v, "filling", None)


class ThanksgivingDinner(BaseModel):
    dessert: Annotated[
        Union[
            Annotated[ApplePie, Tag("apple")],
            Annotated[PumpkinPie, Tag("pumpkin")],
        ],
        Discriminator(get_discriminator_value),
    ]


class GroupedDinner(BaseModel):
    model_config = ConfigDict(group_by="time")

    time: int = Field(alias="time_to_cook")
    dinner: list[ThanksgivingDinner]


class NestedGroupedDinner(BaseModel):
    model_config = ConfigDict(group_by="time")

    time: int = Field(alias="time_to_cook")
    nested: GroupedDinner


data = [
    {"time_to_cook": 1, "fruit": "apple"},
    {"time_to_cook": 2, "filling": "pumpkin"},
]

aggregation_data = [
    {"time_to_cook": 1, "fruit": "apple"},
    {"time_to_cook": 1, "filling": "pumpkin"},
    {"time_to_cook": 2, "filling": "pumpkin"},
]


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params: list[Parameter] = [
    Parameter(
        model=ThanksgivingDinner,
        data=data,
        bindings=snapshot(
            [
                {"dessert": {"fruit": "apple", "time_to_cook": 1, "filling": None}},
                {"dessert": {"fruit": None, "time_to_cook": 2, "filling": "pumpkin"}},
            ]
        ),
        model_dump=snapshot(
            [
                {"dessert": {"time_to_cook": 1, "fruit": "apple"}},
                {"dessert": {"time_to_cook": 2, "filling": "pumpkin"}},
            ]
        ),
    ),
    Parameter(
        model=GroupedDinner,
        data=aggregation_data,
        bindings=snapshot(
            [
                {
                    "time_to_cook": 1,
                    "dinner": [
                        {
                            "dessert": {
                                "fruit": "apple",
                                "time_to_cook": 1,
                                "filling": None,
                            }
                        },
                        {
                            "dessert": {
                                "fruit": None,
                                "time_to_cook": 1,
                                "filling": "pumpkin",
                            }
                        },
                    ],
                },
                {
                    "time_to_cook": 2,
                    "dinner": [
                        {
                            "dessert": {
                                "fruit": None,
                                "time_to_cook": 2,
                                "filling": "pumpkin",
                            }
                        }
                    ],
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "time": 1,
                    "dinner": [
                        {"dessert": {"time_to_cook": 1, "fruit": "apple"}},
                        {"dessert": {"time_to_cook": 1, "filling": "pumpkin"}},
                    ],
                },
                {
                    "time": 2,
                    "dinner": [{"dessert": {"time_to_cook": 2, "filling": "pumpkin"}}],
                },
            ]
        ),
    ),
    Parameter(
        model=NestedGroupedDinner,
        data=aggregation_data,
        bindings=snapshot(
            [
                {
                    "time_to_cook": 1,
                    "nested": {
                        "time_to_cook": 1,
                        "dinner": [
                            {
                                "dessert": {
                                    "fruit": "apple",
                                    "time_to_cook": 1,
                                    "filling": None,
                                }
                            },
                            {
                                "dessert": {
                                    "fruit": None,
                                    "time_to_cook": 1,
                                    "filling": "pumpkin",
                                }
                            },
                        ],
                    },
                },
                {
                    "time_to_cook": 2,
                    "nested": {
                        "time_to_cook": 2,
                        "dinner": [
                            {
                                "dessert": {
                                    "fruit": None,
                                    "time_to_cook": 2,
                                    "filling": "pumpkin",
                                }
                            }
                        ],
                    },
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "time": 1,
                    "nested": {
                        "time": 1,
                        "dinner": [
                            {"dessert": {"time_to_cook": 1, "fruit": "apple"}},
                            {"dessert": {"time_to_cook": 1, "filling": "pumpkin"}},
                        ],
                    },
                },
                {
                    "time": 2,
                    "nested": {
                        "time": 2,
                        "dinner": [
                            {"dessert": {"time_to_cook": 2, "filling": "pumpkin"}}
                        ],
                    },
                },
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_callable_discriminated_union(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)
    assert list(materializer.generate_bindings()) == param.bindings
    assert [m.model_dump() for m in materializer.generate_models()] == param.model_dump


def test_callable_discriminated_union_model_types():
    apple, pumpkin = ModelMaterializer(
        model=ThanksgivingDinner, data=data
    ).generate_models()
    assert isinstance(apple.dessert, ApplePie)
    assert isinstance(pumpkin.dessert, PumpkinPie)
