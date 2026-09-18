from typing import Annotated, Literal

import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Field
from tests.materializer.param import Expected, Parameter

data = [
    {"pet_type": "cat", "n": 1},
    {"pet_type": "dog", "n": 2},
    {"pet_type": "lizard", "n": 3},
    {"pet_type": "reptile", "n": 4},
]

data_n_group = [
    {"pet_type": "cat", "n": 1},
    {"pet_type": "dog", "n": 1},
    {"pet_type": "lizard", "n": 3},
    {"pet_type": "reptile", "n": 4},
]


class Cat(BaseModel):
    kind: Literal["cat"] = Field(alias="pet_type")


class Dog(BaseModel):
    kind: Literal["dog"] = Field(alias="pet_type")


class Lizard(BaseModel):
    kind: Literal["reptile", "lizard"] = Field(alias="pet_type")


class Model1(BaseModel):
    pet: Annotated[Cat | Dog | Lizard, Field(discriminator="kind")]
    n: int


class Model2(BaseModel):
    nested: Model1


class Model3(BaseModel):
    model_config = ConfigDict(group_by="n")

    n: int
    agg: list[Model1]


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            bindings=[
                {"n": 1, "pet": {"pet_type": "cat"}},
                {"n": 2, "pet": {"pet_type": "dog"}},
                {"n": 3, "pet": {"pet_type": "lizard"}},
                {"n": 4, "pet": {"pet_type": "reptile"}},
            ],
            model_dump=[
                {"pet": {"kind": "cat"}, "n": 1},
                {"pet": {"kind": "dog"}, "n": 2},
                {"pet": {"kind": "lizard"}, "n": 3},
                {"pet": {"kind": "reptile"}, "n": 4},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"n": 1, "pet": {"pet_type": "cat"}}},
                {"nested": {"n": 2, "pet": {"pet_type": "dog"}}},
                {"nested": {"n": 3, "pet": {"pet_type": "lizard"}}},
                {"nested": {"n": 4, "pet": {"pet_type": "reptile"}}},
            ],
            model_dump=[
                {"nested": {"pet": {"kind": "cat"}, "n": 1}},
                {"nested": {"pet": {"kind": "dog"}, "n": 2}},
                {"nested": {"pet": {"kind": "lizard"}, "n": 3}},
                {"nested": {"pet": {"kind": "reptile"}, "n": 4}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data_n_group},
        expected=Expected(
            bindings=[
                {
                    "n": 1,
                    "agg": [
                        {"n": 1, "pet": {"pet_type": "cat"}},
                        {"n": 1, "pet": {"pet_type": "dog"}},
                    ],
                },
                {"n": 3, "agg": [{"n": 3, "pet": {"pet_type": "lizard"}}]},
                {"n": 4, "agg": [{"n": 4, "pet": {"pet_type": "reptile"}}]},
            ],
            model_dump=[
                {
                    "n": 1,
                    "agg": [
                        {"pet": {"kind": "cat"}, "n": 1},
                        {"pet": {"kind": "dog"}, "n": 1},
                    ],
                },
                {"n": 3, "agg": [{"pet": {"kind": "lizard"}, "n": 3}]},
                {"n": 4, "agg": [{"pet": {"kind": "reptile"}, "n": 4}]},
            ],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_string_discriminated_union(param):

    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
