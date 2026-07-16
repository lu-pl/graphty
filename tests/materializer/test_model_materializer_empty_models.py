import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel
from tests.materializer.param import Expected, Parameter


class Model1(BaseModel):
    pass


class Model2(BaseModel):
    nested: Model1


class Model3(BaseModel):
    nested: Model2


class Model4(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model1


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model2


class Model6(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model3


class Model7(BaseModel):
    nested: Model4


class Model8(BaseModel):
    model_config = ConfigDict(group_by="y")

    y: int
    nested: list[Model1]


class Model9(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: list[Model8]


class Model10(BaseModel):
    """This model shows an interesting edge case
    that leads to potentially unexpected deduplication behavior.

    Note the mode_dump for "nested": [{"x": 1, "nested": {}}, {"x": 1, "nested": {}}];
    usually, those structs would get deduplicated on the Polars-level, so why are there duplicates?

    The answer lies in the fact, that for empty models, the entire projection is forwareded to the model;
    this way, validators get a chance to act upon the raw data and the behavior is consistent with
    empty top-level models.

    Looking at the bindings data which then gets the raw data of the current context,
    "nested": [
                  {"x": 1, "nested": {"y": 2, "x": 1, "z": 3}},
                  {"x": 1, "nested": {"y": 3, "x": 1, "z": 4}},
              ]
    shows, that in fact, the data is distinct and ergo does not get deduplicated on the Polars-level.

    Note that this is an edge case and does not invalidate the general behavior of forwarding raw data
    to empty models conceptually.
    """

    model_config = ConfigDict(group_by="x")

    x: int
    nested: list[Model4]


data = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 1, "y": 3, "z": 4},
    {"x": 2, "y": 4, "z": 5},
]

params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=Expected(
            bindings=[
                {"x": 1, "y": 2, "z": 3},
                {"x": 1, "y": 3, "z": 4},
                {"x": 2, "y": 4, "z": 5},
            ],
            model_dump=[{}, {}, {}],
        ),
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"y": 2, "x": 1, "z": 3}},
                {"nested": {"y": 3, "x": 1, "z": 4}},
                {"nested": {"y": 4, "x": 2, "z": 5}},
            ],
            model_dump=[{"nested": {}}, {"nested": {}}, {"nested": {}}],
        ),
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"nested": {"y": 2, "x": 1, "z": 3}}},
                {"nested": {"nested": {"y": 3, "x": 1, "z": 4}}},
                {"nested": {"nested": {"y": 4, "x": 2, "z": 5}}},
            ],
            model_dump=[
                {"nested": {"nested": {}}},
                {"nested": {"nested": {}}},
                {"nested": {"nested": {}}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=Expected(
            bindings=[
                {"x": 1, "nested": {"y": 2, "x": 1, "z": 3}},
                {"x": 2, "nested": {"y": 4, "x": 2, "z": 5}},
            ],
            model_dump=[{"x": 1, "nested": {}}, {"x": 2, "nested": {}}],
        ),
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=Expected(
            bindings=[
                {"x": 1, "nested": {"nested": {"y": 2, "x": 1, "z": 3}}},
                {"x": 2, "nested": {"nested": {"y": 4, "x": 2, "z": 5}}},
            ],
            model_dump=[
                {"x": 1, "nested": {"nested": {}}},
                {"x": 2, "nested": {"nested": {}}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=Expected(
            bindings=[
                {"x": 1, "nested": {"nested": {"nested": {"y": 2, "x": 1, "z": 3}}}},
                {"x": 2, "nested": {"nested": {"nested": {"y": 4, "x": 2, "z": 5}}}},
            ],
            model_dump=[
                {"x": 1, "nested": {"nested": {"nested": {}}}},
                {"x": 2, "nested": {"nested": {"nested": {}}}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=Expected(
            bindings=[
                {"nested": {"x": 1, "nested": {"y": 2, "x": 1, "z": 3}}},
                {"nested": {"x": 1, "nested": {"y": 3, "x": 1, "z": 4}}},
                {"nested": {"x": 2, "nested": {"y": 4, "x": 2, "z": 5}}},
            ],
            model_dump=[
                {"nested": {"x": 1, "nested": {}}},
                {"nested": {"x": 1, "nested": {}}},
                {"nested": {"x": 2, "nested": {}}},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model9, "data": data},
        expected=Expected(
            bindings=[
                {
                    "x": 1,
                    "nested": [
                        {"y": 2, "nested": [{"y": 2, "x": 1, "z": 3}]},
                        {"y": 3, "nested": [{"y": 3, "x": 1, "z": 4}]},
                    ],
                },
                {"x": 2, "nested": [{"y": 4, "nested": [{"y": 4, "x": 2, "z": 5}]}]},
            ],
            model_dump=[
                {
                    "x": 1,
                    "nested": [{"y": 2, "nested": [{}]}, {"y": 3, "nested": [{}]}],
                },
                {"x": 2, "nested": [{"y": 4, "nested": [{}]}]},
            ],
        ),
    ),
    Parameter(
        kwargs={"model": Model10, "data": data},
        expected=Expected(
            bindings=[
                {
                    "x": 1,
                    "nested": [
                        {"x": 1, "nested": {"y": 2, "x": 1, "z": 3}},
                        {"x": 1, "nested": {"y": 3, "x": 1, "z": 4}},
                    ],
                },
                {"x": 2, "nested": [{"x": 2, "nested": {"y": 4, "x": 2, "z": 5}}]},
            ],
            model_dump=[
                {"x": 1, "nested": [{"x": 1, "nested": {}}, {"x": 1, "nested": {}}]},
                {"x": 2, "nested": [{"x": 2, "nested": {}}]},
            ],
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_empty_models(param):

    materializer = ModelMaterializer(**param.kwargs)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.expected.bindings
    assert model_dump == param.expected.model_dump
