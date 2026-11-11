"""Tests for graphty's custom exceptions."""

import copy
import pickle
from collections.abc import Callable
from typing import NamedTuple, cast

import pytest
from graphty.utils.exceptions import (
    AliasResolutionError,
    InvalidGroupByError,
    MissingDiscriminatorError,
    MissingGroupByError,
)
from inline_snapshot import snapshot
from pydantic import BaseModel
from typing_extensions import TypeForm


class Model1(BaseModel):
    x: int


class Model2(BaseModel):
    y: int


class ExceptionTestParameter(NamedTuple):
    exception: Exception
    expected_message: str


params: list[ExceptionTestParameter] = [
    ExceptionTestParameter(
        exception=MissingGroupByError(model=Model1),
        expected_message=snapshot(
            "Model 'Model1' with aggregation target does not specify ConfigDict.group_by."
        ),
    ),
    ExceptionTestParameter(
        exception=InvalidGroupByError(model=Model1, group_by_value="y"),
        expected_message=snapshot(
            "Invalid grouping key 'y' for 'Model1'. Grouping keys must reference scalar model fields."
        ),
    ),
    ExceptionTestParameter(
        exception=MissingDiscriminatorError(type_form=cast(TypeForm, Model1 | Model2)),
        expected_message=snapshot(
            "Multi-Model unions must be discriminated unions. Unable to extract discriminator for union type 'tests.utils.test_exceptions.Model1 | tests.utils.test_exceptions.Model2'."
        ),
    ),
    ExceptionTestParameter(
        exception=AliasResolutionError(
            field_name="x", model=Model1, aliases=["a", "b"], projection=set()
        ),
        expected_message=snapshot(
            "Unable to resolve AliasChoice for field 'x' of model 'Model1': Empty or missing input data projection."
        ),
    ),
    ExceptionTestParameter(
        exception=AliasResolutionError(
            field_name="x", model=Model1, aliases=["a", "b"], projection={"c"}
        ),
        expected_message=snapshot(
            "Unable to resolve AliasChoice for field 'x' of model 'Model1': None of computed aliases '['a', 'b']' in input data projection '{'c'}'."
        ),
    ),
]

clone_functions: list[Callable[[Exception], Exception]] = [
    copy.copy,
    copy.deepcopy,
    lambda exception: pickle.loads(pickle.dumps(exception)),
]


@pytest.mark.parametrize("param", params)
def test_exception_message(param: ExceptionTestParameter) -> None:
    assert str(param.exception) == param.expected_message


@pytest.mark.parametrize("clone", clone_functions)
@pytest.mark.parametrize("param", params)
def test_exception_clone(
    param: ExceptionTestParameter, clone: Callable[[Exception], Exception]
) -> None:
    cloned: Exception = clone(param.exception)

    assert type(cloned) is type(param.exception)
    assert vars(cloned) == vars(param.exception)
    assert str(cloned) == str(param.exception)
