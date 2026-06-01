from graphty.planner import ConfigDict, LazyFramePlanner
from pydantic import BaseModel


class DeeplyNested(BaseModel):
    model_config = ConfigDict(group_by="x")

    y: list[int]


class Nested(BaseModel):
    y: int
    deeply_nested: DeeplyNested


class Model(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    model: DeeplyNested
    aggr: list[Nested]


EXPECTED = [
    {
        "x": 1,
        "y": 2,
        "model": {"x": 1, "y": [2, 3]},
        "aggr": [
            {"x": 1, "y": 2, "deeply_nested": {"x": 1, "y": [2, 3]}},
            {"x": 1, "y": 3, "deeply_nested": {"x": 1, "y": [2, 3]}},
        ],
    },
    {
        "x": 3,
        "y": 4,
        "model": {"x": 3, "y": [4]},
        "aggr": [{"x": 3, "y": 4, "deeply_nested": {"x": 3, "y": [4]}}],
    },
]


def test_planner_ungrouped_nested():
    bindings = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 3, "y": 4}]

    planner = LazyFramePlanner(model=Model, bindings=bindings)
    frame = planner.run()

    assert frame.collect().to_dicts() == EXPECTED
