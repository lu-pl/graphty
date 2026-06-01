from typing import Annotated, Literal, Union

import pytest
from graphty.planner import LazyFramePlanner
from pydantic import BaseModel, Field


class Cat(BaseModel):
    pet_type: Literal["cat"]


class Dog(BaseModel):
    pet_type: Literal["dog"]


class Lizard(BaseModel):
    pet_type: Literal["reptile", "lizard"]


class Model1(BaseModel):
    pet: Annotated[Cat | Dog | Lizard, Field(discriminator="pet_type")]
    n: int


class Model2(BaseModel):
    pet: Annotated[Union[Cat, Dog, Lizard], Field(discriminator="pet_type")]
    n: int


class Model3(BaseModel):
    pet: Cat | Dog | Lizard = Field(discriminator="pet_type")
    n: int


class Model4(BaseModel):
    pet: Union[Cat, Dog, Lizard] = Field(discriminator="pet_type")
    n: int


EXPECTED = [
    {"pet_type": "cat", "n": 1, "pet": {"pet_type": "cat", "n": 1}},
    {"pet_type": "dog", "n": 2, "pet": {"pet_type": "dog", "n": 2}},
    {"pet_type": "lizard", "n": 3, "pet": {"pet_type": "lizard", "n": 3}},
    {"pet_type": "reptile", "n": 4, "pet": {"pet_type": "reptile", "n": 4}},
]


@pytest.mark.parametrize("model", [Model1, Model2, Model3, Model4])
def test_planner_string_discriminated(model):
    data = [
        {"pet_type": "cat", "n": 1},
        {"pet_type": "dog", "n": 2},
        {"pet_type": "lizard", "n": 3},
        {"pet_type": "reptile", "n": 4},
    ]

    planner = LazyFramePlanner(model=model, data=data)
    frame = planner.run()

    assert frame.collect().to_dicts() == EXPECTED
