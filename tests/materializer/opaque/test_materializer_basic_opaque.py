from dataclasses import dataclass
from typing import Annotated

import pytest
from graphty import ConfigDict, ModelMaterializer, Opaque
from inline_snapshot import snapshot
from pydantic import BaseModel


class Model1(BaseModel):
    x: Annotated[object, Opaque()]


class Model2(BaseModel):
    x: Annotated[int, Opaque()]
    y: Annotated[int, Opaque()]


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    y: Annotated[object, Opaque()]


class Model4(BaseModel):
    nested: Model1


class Model5(BaseModel):
    nested: Model2


class Model6(BaseModel):
    """Note: Outer model is grouped, `nested` is not aggregated;
    that means that the planner applies the `pl.Expr.first` default
    before the planner is disengaged in Model1.

    This is the reason why `first` semantics apply to the Opaque field,
    singular rows is simply the raw data the planner has access to at that time.
    """

    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model1


class Model7(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model2


class Model8(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: list[Model1]


class Model9(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: list[Model2]


class Model10(BaseModel):
    raw: Annotated[object, Opaque()]


class Model11(BaseModel):
    nested: Model10


data = [
    {"x": 1, "y": 2},
    {"x": 1, "y": 3},
    {"x": 2, "y": 4},
]


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object


params: list[Parameter] = [
    Parameter(
        model=Model1,
        data=data,
        bindings=snapshot(
            [{"x": {"y": 2, "x": 1}}, {"x": {"y": 3, "x": 1}}, {"x": {"y": 4, "x": 2}}]
        ),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot(
            [
                {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}},
                {"x": {"y": 3, "x": 1}, "y": {"y": 3, "x": 1}},
                {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}},
            ]
        ),
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=snapshot(
            [
                {"x": 1, "y": [{"y": 2, "x": 1}, {"y": 3, "x": 1}]},
                {"x": 2, "y": [{"y": 4, "x": 2}]},
            ]
        ),
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=snapshot(
            [
                {"nested": {"x": {"y": 2, "x": 1}}},
                {"nested": {"x": {"y": 3, "x": 1}}},
                {"nested": {"x": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=snapshot(
            [
                {"nested": {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}}},
                {"nested": {"x": {"y": 3, "x": 1}, "y": {"y": 3, "x": 1}}},
                {"nested": {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        model=Model6,
        data=data,
        bindings=snapshot(
            [
                {"x": 1, "nested": {"x": {"y": 2, "x": 1}}},
                {"x": 2, "nested": {"x": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        model=Model7,
        data=data,
        bindings=snapshot(
            [
                {"x": 1, "nested": {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}}},
                {"x": 2, "nested": {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        model=Model8,
        data=data,
        bindings=snapshot(
            [
                {"x": 1, "nested": [{"x": {"y": 2, "x": 1}}, {"x": {"y": 3, "x": 1}}]},
                {"x": 2, "nested": [{"x": {"y": 4, "x": 2}}]},
            ]
        ),
    ),
    Parameter(
        model=Model9,
        data=data,
        bindings=snapshot(
            [
                {
                    "x": 1,
                    "nested": [
                        {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}},
                        {"x": {"y": 3, "x": 1}, "y": {"y": 3, "x": 1}},
                    ],
                },
                {"x": 2, "nested": [{"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}}]},
            ]
        ),
    ),
    Parameter(
        model=Model10,
        data=data,
        bindings=snapshot(
            [
                {"raw": {"y": 2, "x": 1}},
                {"raw": {"y": 3, "x": 1}},
                {"raw": {"y": 4, "x": 2}},
            ]
        ),
    ),
    Parameter(
        model=Model11,
        data=data,
        bindings=snapshot(
            [
                {"nested": {"raw": {"y": 2, "x": 1}}},
                {"nested": {"raw": {"y": 3, "x": 1}}},
                {"nested": {"raw": {"y": 4, "x": 2}}},
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_opaque_basic(param):
    """Only `generate_bindings()` is checked here: `Opaque()` disengages the
    planner (which forwards the raw struct regardless of the field's declared
    type), not Pydantic. What happens on `generate_models()` for a
    concretely-typed opaque field without a before-validator is Pydantic's own
    type validation behaving exactly as documented, not graphty-specific logic.
    """

    materializer = ModelMaterializer(model=param.model, data=param.data)
    bindings = list(materializer.generate_bindings())

    assert bindings == param.bindings
