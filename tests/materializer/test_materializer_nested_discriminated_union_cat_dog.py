from typing import Annotated, Literal, Union

import pytest
from graphty import ModelMaterializer
from pydantic import BaseModel, Field
from tests.materializer.param import Expected, Parameter


class BlackCat(BaseModel):
    pet_type: Literal["cat"]
    color: Literal["black"]
    name: str


class WhiteCat(BaseModel):
    pet_type: Literal["cat"]
    color: Literal["white"]
    name: str


Cat = Annotated[Union[BlackCat, WhiteCat], Field(discriminator="color")]


class Dog(BaseModel):
    pet_type: Literal["dog"]
    name: str


Pet = Annotated[Union[Cat, Dog], Field(discriminator="pet_type")]


class Model(BaseModel):
    pet: Pet


data = [
    {"pet_type": "cat", "color": "black", "name": "felix"},
    {"pet_type": "cat", "color": "white", "name": "muzi"},
    {"pet_type": "dog", "color": None, "name": "arcanine"},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model, "data": data},
        expected=Expected(
            bindings=[
                {"pet": {"name": "felix", "pet_type": "cat", "color": "black"}},
                {"pet": {"name": "muzi", "pet_type": "cat", "color": "white"}},
                {"pet": {"name": "arcanine", "pet_type": "dog", "color": None}},
            ],
            model_dump=[
                {"pet": {"pet_type": "cat", "color": "black", "name": "felix"}},
                {"pet": {"pet_type": "cat", "color": "white", "name": "muzi"}},
                {"pet": {"pet_type": "dog", "name": "arcanine"}},
            ],
        ),
    )
]


@pytest.mark.parametrize("param", params)
def test_materializer_nested_discriminated_unions_cat_dog_bindings_dump(param):
    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump


@pytest.mark.parametrize("param", params)
def test_materializer_nested_discriminated_unions_cat_dog_model(param):
    materializer = ModelMaterializer(**param.kwargs)

    black_cat, white_cat, dog = materializer.generate_models()
    assert isinstance(black_cat.pet, BlackCat)
    assert isinstance(white_cat.pet, WhiteCat)
    assert isinstance(dog.pet, Dog)
