from typing import Annotated, Any, Literal, Optional, Union

from graphty.planner import LazyFramePlanner
from pydantic import BaseModel, Discriminator, Tag


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


EXPECTED = [
    {
        "dessert": {"time_to_cook": 1, "fruit": "apple", "filling": None},
    },
    {
        "dessert": {"time_to_cook": 2, "fruit": None, "filling": "pumpkin"},
    },
]


def test_planner_callable_discriminated_union():
    data = [
        {"time_to_cook": 1, "fruit": "apple"},
        {"time_to_cook": 2, "filling": "pumpkin"},
    ]
    planner = LazyFramePlanner(model=ThanksgivingDinner, data=data)
    frame = planner.run().collect()

    assert frame.to_dicts() == EXPECTED
