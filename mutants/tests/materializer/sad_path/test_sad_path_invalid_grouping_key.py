import pytest
from graphty import ConfigDict, InvalidGroupByError, ModelMaterializer
from pydantic import BaseModel, Field

data = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 1, "y": 3, "z": 4},
    {"x": 2, "y": 4, "z": 5},
]


class Nested(BaseModel):
    z: int


class Model1(BaseModel):
    model_config = ConfigDict(group_by="dne")

    x: int
    y: list[int]


class Model2(BaseModel):
    model_config = ConfigDict(group_by="y")

    x: int
    y: list[int]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="z")

    x: int
    y: list[int]
    z: Nested


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    y: list[int]


class Model5(BaseModel):
    """Grouping keys must reference *model fields*, not aliases."""

    model_config = ConfigDict(group_by="z")

    x: int = Field(alias="z")
    y: list[int]


models: list[type[BaseModel]] = [
    Model1,
    Model2,
    Model3,
    Model4,
    Model5,
]


@pytest.mark.parametrize("model", models)
def test_sad_path_invalid_grouping_key(model):

    with pytest.raises(InvalidGroupByError):
        materializer = ModelMaterializer(model=model, data=data)
        list(materializer.generate_bindings())
