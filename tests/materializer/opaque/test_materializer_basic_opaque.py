from typing import Annotated

import pytest
from graphty import ConfigDict, ModelMaterializer, Opaque
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


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

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            [{"x": {"y": 2, "x": 1}}, {"x": {"y": 3, "x": 1}}, {"x": {"y": 4, "x": 2}}]
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            [
                {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}},
                {"x": {"y": 3, "x": 1}, "y": {"y": 3, "x": 1}},
                {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            [
                {"x": 1, "y": [{"y": 2, "x": 1}, {"y": 3, "x": 1}]},
                {"x": 2, "y": [{"y": 4, "x": 2}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            [
                {"nested": {"x": {"y": 2, "x": 1}}},
                {"nested": {"x": {"y": 3, "x": 1}}},
                {"nested": {"x": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            [
                {"nested": {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}}},
                {"nested": {"x": {"y": 3, "x": 1}, "y": {"y": 3, "x": 1}}},
                {"nested": {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested": {"x": {"y": 2, "x": 1}}},
                {"x": 2, "nested": {"x": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested": {"x": {"y": 2, "x": 1}, "y": {"y": 2, "x": 1}}},
                {"x": 2, "nested": {"x": {"y": 4, "x": 2}, "y": {"y": 4, "x": 2}}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model8, "data": data},
        expected=Expected(
            [
                {"x": 1, "nested": [{"x": {"y": 2, "x": 1}}, {"x": {"y": 3, "x": 1}}]},
                {"x": 2, "nested": [{"x": {"y": 4, "x": 2}}]},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model9, "data": data},
        expected=Expected(
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
        kwargs={"model": Model10, "data": data},
        expected=Expected(
            [
                {"raw": {"y": 2, "x": 1}},
                {"raw": {"y": 3, "x": 1}},
                {"raw": {"y": 4, "x": 2}},
            ]
        ),
    ),
    Parameter(
        kwargs={"model": Model11, "data": data},
        expected=Expected(
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

    materializer = ModelMaterializer(**param.kwargs)
    bindings = list(materializer.generate_bindings())

    assert bindings == param.expected.bindings
