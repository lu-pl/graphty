"""Basic sad path tests for non-discriminated multi model unions."""

from typing import Annotated, Union

import pytest
from graphty import MissingDiscriminatorError, ModelMaterializer
from pydantic import BaseModel


class Nested1(BaseModel): ...


class Nested2(BaseModel): ...


class Model1(BaseModel):
    nested: Nested1 | Nested2


class Model2(BaseModel):
    nested: Union[Nested1, Nested2]


class Model3(BaseModel):
    nested: Annotated[Nested1 | Nested2, ""]


@pytest.mark.parametrize("model", [Model1, Model2, Model3])
def test_sad_path_multi_model_union(model):
    data = [
        {"some": "data"}
    ]  # non-empty pseudo data to prevent early exit in LazyFrame.run
    materializer = ModelMaterializer(model=model, data=data)

    with pytest.raises(MissingDiscriminatorError):
        list(materializer.generate_bindings())
