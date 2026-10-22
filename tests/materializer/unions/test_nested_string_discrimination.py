"""Basic test for nested string discriminated unions.

Covers:
- Two levels of string discriminated unions
  (Cat in Cat | Dog is itself a discriminated union)
- Discrimnated union model aggregation (top-level + nested union aggregation)
"""

from dataclasses import dataclass
from typing import Annotated, Literal, Union

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Field


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


class GroupedPet(BaseModel):
    model_config = ConfigDict(group_by="pet_type")

    pet_type: str
    pet: list[Pet]


class NestedGroupedPet(BaseModel):
    model_config = ConfigDict(group_by="pet_type")

    pet_type: str
    nested: list[GroupedPet]


data = [
    {"pet_type": "cat", "color": "black", "name": "felix"},
    {"pet_type": "cat", "color": "white", "name": "muzi"},
    {"pet_type": "dog", "color": None, "name": "arcanine"},
]


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params: list[Parameter] = [
    Parameter(
        model=Model,
        data=data,
        bindings=snapshot(
            [
                {"pet": {"name": "felix", "pet_type": "cat", "color": "black"}},
                {"pet": {"name": "muzi", "pet_type": "cat", "color": "white"}},
                {"pet": {"name": "arcanine", "pet_type": "dog", "color": None}},
            ]
        ),
        model_dump=snapshot(
            [
                {"pet": {"pet_type": "cat", "color": "black", "name": "felix"}},
                {"pet": {"pet_type": "cat", "color": "white", "name": "muzi"}},
                {"pet": {"pet_type": "dog", "name": "arcanine"}},
            ]
        ),
    ),
    Parameter(
        model=GroupedPet,
        data=data,
        bindings=snapshot(
            [
                {
                    "pet_type": "cat",
                    "pet": [
                        {"name": "felix", "pet_type": "cat", "color": "black"},
                        {"name": "muzi", "pet_type": "cat", "color": "white"},
                    ],
                },
                {
                    "pet_type": "dog",
                    "pet": [{"name": "arcanine", "pet_type": "dog", "color": None}],
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "pet_type": "cat",
                    "pet": [
                        {"pet_type": "cat", "color": "black", "name": "felix"},
                        {"pet_type": "cat", "color": "white", "name": "muzi"},
                    ],
                },
                {"pet_type": "dog", "pet": [{"pet_type": "dog", "name": "arcanine"}]},
            ]
        ),
    ),
    Parameter(
        model=NestedGroupedPet,
        data=data,
        bindings=snapshot(
            [
                {
                    "pet_type": "cat",
                    "nested": [
                        {
                            "pet_type": "cat",
                            "pet": [
                                {"name": "felix", "pet_type": "cat", "color": "black"},
                                {"name": "muzi", "pet_type": "cat", "color": "white"},
                            ],
                        }
                    ],
                },
                {
                    "pet_type": "dog",
                    "nested": [
                        {
                            "pet_type": "dog",
                            "pet": [
                                {"name": "arcanine", "pet_type": "dog", "color": None}
                            ],
                        }
                    ],
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "pet_type": "cat",
                    "nested": [
                        {
                            "pet_type": "cat",
                            "pet": [
                                {"pet_type": "cat", "color": "black", "name": "felix"},
                                {"pet_type": "cat", "color": "white", "name": "muzi"},
                            ],
                        }
                    ],
                },
                {
                    "pet_type": "dog",
                    "nested": [
                        {
                            "pet_type": "dog",
                            "pet": [{"pet_type": "dog", "name": "arcanine"}],
                        }
                    ],
                },
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_nested_str_discriminated_union(param):
    materializer = ModelMaterializer(model=param.model, data=param.data)
    assert list(materializer.generate_bindings()) == param.bindings
    assert [m.model_dump() for m in materializer.generate_models()] == param.model_dump


def test_nested_str_discriminated_union_model_types():
    black_cat, white_cat, dog = ModelMaterializer(
        model=Model, data=data
    ).generate_models()
    assert isinstance(black_cat.pet, BlackCat)
    assert isinstance(white_cat.pet, WhiteCat)
    assert isinstance(dog.pet, Dog)
