import pytest
from graphty import ConfigDict, ModelMaterializer
from pydantic import BaseModel, Field, ValidationError
from tests.materializer.param import Expected, ExpectedException, Parameter


class Model1(BaseModel):
    dne: int


class Model2(BaseModel):
    nested: Model1


class Model3(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    dne: int


class Model4(BaseModel):
    nested: Model3


class Model5(BaseModel):
    model_config = ConfigDict(group_by="x")

    x: int
    nested: Model3


class Model6(BaseModel):
    x: int = Field(alias="ALIAS")


class Model7(BaseModel):
    nested: Model6


data = [
    {"x": 1},
    {"x": 2},
    {"x": 3},
]


params: list[Parameter] = [
    Parameter(
        kwargs={"model": Model1, "data": data},
        expected=[
            Expected(bindings=[{"x": 1}, {"x": 2}, {"x": 3}]),
            ExpectedException(
                exception=ValidationError, match="1 validation error for Model1\ndne"
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model2, "data": data},
        expected=[
            Expected(
                bindings=[
                    {"nested": {"x": 1}},
                    {"nested": {"x": 2}},
                    {"nested": {"x": 3}},
                ]
            ),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model2\nnested.dne",
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model3, "data": data},
        expected=[
            Expected(bindings=[{"x": 1}, {"x": 2}, {"x": 3}]),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model3\ndne",
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model4, "data": data},
        expected=[
            Expected(
                bindings=[
                    {"nested": {"x": 1}},
                    {"nested": {"x": 2}},
                    {"nested": {"x": 3}},
                ]
            ),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model4\nnested.dne",
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model5, "data": data},
        expected=[
            Expected(
                bindings=[
                    {"x": 1, "nested": {"x": 1}},
                    {"x": 2, "nested": {"x": 2}},
                    {"x": 3, "nested": {"x": 3}},
                ]
            ),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model5\nnested.dne",
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model6, "data": data},
        expected=[
            Expected(bindings=[{"x": 1}, {"x": 2}, {"x": 3}]),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model6\nALIAS",
            ),
        ],
    ),
    Parameter(
        kwargs={"model": Model7, "data": data},
        expected=[
            Expected(
                bindings=[
                    {"nested": {"x": 1}},
                    {"nested": {"x": 2}},
                    {"nested": {"x": 3}},
                ]
            ),
            ExpectedException(
                exception=ValidationError,
                match="1 validation error for Model7\nnested.ALIAS",
            ),
        ],
    ),
]


@pytest.mark.parametrize("param", params)
def test_sad_path_empty_exprs_select(param):
    materializer = ModelMaterializer(**param.kwargs)

    for expected in param.expected:
        match expected:
            case Expected():
                assert list(materializer.generate_bindings()) == expected.bindings
            case ExpectedException():
                with pytest.raises(
                    expected_exception=expected.exception, match=expected.match
                ):
                    list(materializer.generate_models())

            case _:
                assert False, "This should never happen."
