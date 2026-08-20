"""Basic test for callable discriminated unions.

This is the example from the Pydantic docs section on callable discriminated unions;
see https://pydantic.dev/docs/validation/latest/concepts/unions/#discriminated-unions-with-callable-discriminator.

Covers:
- Basic two-member callable discriminated union
"""

from typing import Annotated, Any, Literal, Optional, Union

import pytest
from graphty import ModelMaterializer
from pydantic import BaseModel, Discriminator, Tag
from tests.materializer.param import Expected, Parameter


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


data = [
    {"time_to_cook": 1, "fruit": "apple"},
    {"time_to_cook": 2, "filling": "pumpkin"},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": ThanksgivingDinner, "data": data},
        expected=Expected(
            bindings=[
                {"dessert": {"time_to_cook": 1, "fruit": "apple", "filling": None}},
                {"dessert": {"time_to_cook": 2, "fruit": None, "filling": "pumpkin"}},
            ],
            model_dump=[
                {"dessert": {"time_to_cook": 1, "fruit": "apple"}},
                {"dessert": {"time_to_cook": 2, "filling": "pumpkin"}},
            ],
        ),
    )
]


@pytest.mark.parametrize("param", params)
def test_callable_discriminated_union(param):
    materializer = ModelMaterializer(**param.kwargs)
    assert list(materializer.generate_bindings()) == param.expected.bindings
    assert [
        m.model_dump() for m in materializer.generate_models()
    ] == param.expected.model_dump


def test_callable_discriminated_union_model_types():
    apple, pumpkin = ModelMaterializer(
        model=ThanksgivingDinner, data=data
    ).generate_models()
    assert isinstance(apple.dessert, ApplePie)
    assert isinstance(pumpkin.dessert, PumpkinPie)
