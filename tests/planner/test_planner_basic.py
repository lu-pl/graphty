"""Basic planner tests."""

from typing import NamedTuple

import pytest
from graphty import ConfigDict
from graphty.planner import LazyFramePlanner
from pydantic import BaseModel


class TestParameter(NamedTuple):
    kwargs: dict
    expected: list[dict]


class Model1(BaseModel):
    model_config = ConfigDict(group_by="x")
    y: int


class Model2(BaseModel):
    model_config = ConfigDict(group_by="x")
    x: int
    y: int


data = [{"x": 1, "y": 2}, {"x": 1, "y": 2}]

params: list[TestParameter] = [
    TestParameter(kwargs={"model": Model1, "data": data}, expected=[{"y": 2}]),
    TestParameter(kwargs={"model": Model2, "data": data}, expected=[{"x": 1, "y": 2}]),
]


@pytest.mark.parametrize("param", params)
def test_planner_basic(param):

    planner = LazyFramePlanner(**param.kwargs)
    df = planner.run().collect()

    assert df.to_dicts() == param.expected
