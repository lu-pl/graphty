from typing import Annotated, Any, Literal

import pytest
from graphty import ModelMaterializer
from pydantic import BaseModel, Discriminator, Field, Tag
from tests.materializer.param import Expected, Parameter


class Cat(BaseModel):
    kind: Literal["cat"]


class Dog(BaseModel):
    kind: Literal["dog"]


class Car(BaseModel):
    kind: Literal["car"]


def get_domain(v: Any) -> str:
    kind = v.get("kind") if isinstance(v, dict) else getattr(v, "kind", None)
    if kind in {"cat", "dog"}:
        return "animal"
    return "vehicle"


Animal = Annotated[Cat | Dog, Field(discriminator="kind")]

Thing = Annotated[
    Annotated[Animal, Tag("animal")] | Annotated[Car, Tag("vehicle")],
    Discriminator(get_domain),
]


class Model(BaseModel):
    thing: Thing


data = [
    {"kind": "cat"},
    {"kind": "dog"},
    {"kind": "car"},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model, "data": data},
        expected=Expected(
            bindings=[
                {"thing": {"kind": "cat"}},
                {"thing": {"kind": "dog"}},
                {"thing": {"kind": "car"}},
            ]
        ),
    )
]


@pytest.mark.parametrize("param", params)
def test_materializer_mixed_discriminated_union(param):
    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump


@pytest.mark.parametrize("param", params)
def test_materializer_mixed_discriminated_union_model(param):
    materializer = ModelMaterializer(**param.kwargs)

    cat, dog, car = materializer.generate_models()
    assert isinstance(cat.thing, Cat)
    assert isinstance(dog.thing, Dog)
    assert isinstance(car.thing, Car)
