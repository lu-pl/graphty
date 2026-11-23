"""Basic sad path tests for models with aggregation targets and missing grouping key."""

from typing import NamedTuple

import pytest
from graphty import MissingGroupByError, ModelMaterializer
from pydantic import BaseModel


class Model1(BaseModel):
    # misses group_by!
    x: int
    y: list[int]


class Model2(BaseModel):
    # misses group_by! y is absent from the data and has a default
    x: int
    y: list[int] = []


class MissingGroupByParameter(NamedTuple):
    model: type[BaseModel]
    data: list[dict[str, object]]
    comment: str = ""


params: list[MissingGroupByParameter] = [
    MissingGroupByParameter(
        model=Model1,
        data=[{"x": 1, "y": 2}, {"x": 1, "y": 3}],
    ),
    MissingGroupByParameter(
        model=Model2,
        data=[{"x": 1}, {"x": 1}],
        comment="Missing group_by must not be skipped for absent list columns.",
    ),
]


@pytest.mark.parametrize("param", params)
def test_sad_path_missing_grouping_key(param: MissingGroupByParameter) -> None:
    materializer = ModelMaterializer(model=param.model, data=param.data)

    with pytest.raises(MissingGroupByError):
        list(materializer.generate_models())
