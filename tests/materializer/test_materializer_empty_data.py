import polars as pl
import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel


class Model(BaseModel):
    x: int


class GroupedModel(BaseModel):
    model_config = ConfigDict(group_by="x")
    x: int


data = [
    [],
    {},
    pl.LazyFrame(),
    pl.LazyFrame([]),
    pl.LazyFrame({}),
    pl.LazyFrame(schema={"x": pl.Int64}),
]


@pytest.mark.parametrize("model", [Model, GroupedModel])
@pytest.mark.parametrize("data", data)
def test_materializer_empty_data(model, data):
    materializer = ModelMaterializer(model=model, data=data)

    assert list(materializer.generate_bindings()) == []
    assert [model.model_dump() for model in materializer.generate_models()] == []
