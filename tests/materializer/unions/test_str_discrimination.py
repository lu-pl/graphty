"""Basic test for string discriminated unions.

This is the example from the Pydantic docs section on string discriminated unions;
see https://pydantic.dev/docs/validation/latest/concepts/unions/#discriminated-unions-with-string-discriminators.

Covers:
- Basic string discriminaged unions
- Multi-value Literal discriminators (Lizard model)
- Different union type indicators (Annotated, Union, |)
"""

from typing import Annotated, Literal, Union

import pytest
from graphty import ModelMaterializer
from pydantic import BaseModel, Field
from tests.materializer.param import Expected, Parameter


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


data = [
    {"pet_type": "cat", "n": 1},
    {"pet_type": "dog", "n": 2},
    {"pet_type": "lizard", "n": 3},
    {"pet_type": "reptile", "n": 4},
]

EXPECTED_BINDINGS = [
    {"n": 1, "pet": {"pet_type": "cat"}},
    {"n": 2, "pet": {"pet_type": "dog"}},
    {"n": 3, "pet": {"pet_type": "lizard"}},
    {"n": 4, "pet": {"pet_type": "reptile"}},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(bindings=EXPECTED_BINDINGS),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(bindings=EXPECTED_BINDINGS),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(bindings=EXPECTED_BINDINGS),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(bindings=EXPECTED_BINDINGS),
    ),
]


@pytest.mark.parametrize("param", params)
def test_str_discriminated_union(param):
    materializer = ModelMaterializer(**param.kwargs)
    assert list(materializer.generate_bindings()) == param.expected.bindings
    assert [
        m.model_dump() for m in materializer.generate_models()
    ] == param.expected.model_dump


def test_str_discriminated_union_model_types():
    cat, dog, lizard, reptile = ModelMaterializer(
        model=Model1, data=data
    ).generate_models()
    assert isinstance(cat.pet, Cat)
    assert isinstance(dog.pet, Dog)
    assert isinstance(lizard.pet, Lizard)
    assert isinstance(reptile.pet, Lizard)
