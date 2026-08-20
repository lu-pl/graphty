"""Tests for mixed string/callable discriminated unions.

Covers:
- Callable discriminated union where one tag point to simple model
  and another points to a nested str discriminated union.
- Bug fix in commit 56888aebda7ff43e2fe2ba5b9e0f25f1e4aeb83b;
  the bug described in https://github.com/lu-pl/graphty/issues/63 needs three conditions:
  A top-level callable-discriminated union with a nested union member and a simple model member.
"""

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
            ],
            model_dump=[
                {"thing": {"kind": "cat"}},
                {"thing": {"kind": "dog"}},
                {"thing": {"kind": "car"}},
            ],
        ),
    )
]


@pytest.mark.parametrize("param", params)
def test_mixed_discriminated_union(param):
    materializer = ModelMaterializer(**param.kwargs)
    assert list(materializer.generate_bindings()) == param.expected.bindings
    assert [
        m.model_dump() for m in materializer.generate_models()
    ] == param.expected.model_dump


def test_mixed_discriminated_union_model_types():
    cat, dog, car = ModelMaterializer(model=Model, data=data).generate_models()
    assert isinstance(cat.thing, Cat)
    assert isinstance(dog.thing, Dog)
    assert isinstance(car.thing, Car)
