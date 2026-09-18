"""Basic sad path tests for models with aggregation targets and missing grouping key."""

import pytest
from graphty import MissingGroupByError, ModelMaterializer
from pydantic import BaseModel


class Model(BaseModel):
    # misses group_by!
    x: int
    y: list[int]


def test_sad_path_missing_grouping_key():
    data = [{"x": 1, "y": 2}, {"x": 1, "y": 3}]
    materializer = ModelMaterializer(model=Model, data=data)

    with pytest.raises(MissingGroupByError):
        list(materializer.generate_models())
