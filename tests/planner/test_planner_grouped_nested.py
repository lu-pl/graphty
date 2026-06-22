from typing import Annotated

import pytest
from graphty import ConfigDict
from graphty.planner import LazyFramePlanner
from pydantic import BaseModel


class DeeplyNested(BaseModel):
    model_config = ConfigDict(group_by="x")

    y: list[int]


class Nested(BaseModel):
    y: int
    deeply_nested: DeeplyNested


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Nested]


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Nested | None]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: Annotated[list[Nested | None], ""]


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Annotated[Nested | None, ""]]


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: Annotated[list[Annotated[Nested | None, ""]], ""]


EXPECTED = [
    {
        "x": 1,
        "model": {"y": [2, 3]},
        "aggr": [
            {"y": 2, "deeply_nested": {"y": [2, 3]}},
            {"y": 3, "deeply_nested": {"y": [2, 3]}},
        ],
    },
    {
        "x": 3,
        "model": {"y": [4]},
        "aggr": [{"y": 4, "deeply_nested": {"y": [4]}}],
    },
]


@pytest.mark.parametrize("model", [Model1, Model2, Model3, Model4, Model5])
def test_planner_grouped_nested(model):
    data = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 3, "y": 4}]

    planner = LazyFramePlanner(model=model, data=data)
    frame = planner.run().collect()

    dicts = frame.to_dicts()
    assert dicts == EXPECTED

    for binding in dicts:
        assert model.model_validate(binding)
