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
        "model": {"y": [2, 3]},
        "aggr": [
            {"y": 2, "deeply_nested": {"y": [2, 3]}},
            {"y": 3, "deeply_nested": {"y": [2, 3]}},
        ],
    },
    {
        "x": 3,
        "y": 4,
        "model": {"y": [4]},
        "aggr": [{"y": 4, "deeply_nested": {"y": [4]}}],
    },
]


def test_planner_grouped_nested():
    data = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 3, "y": 4}]

    planner = LazyFramePlanner(model=Model, data=data)
    frame = planner.run().collect()

    dicts = frame.to_dicts()
    assert dicts == EXPECTED

    for binding in dicts:
        assert Model.model_validate(binding)
