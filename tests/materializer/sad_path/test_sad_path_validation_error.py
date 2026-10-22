from dataclasses import dataclass

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel, Field, ValidationError


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


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    exception_message: object


params: list[Parameter] = [
    Parameter(
        model=Model1,
        data=data,
        bindings=snapshot([{"x": 1}, {"x": 2}, {"x": 3}]),
        exception_message=snapshot("""\
1 validation error for Model1
dne
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model2,
        data=data,
        bindings=snapshot(
            [{"nested": {"x": 1}}, {"nested": {"x": 2}}, {"nested": {"x": 3}}]
        ),
        exception_message=snapshot("""\
1 validation error for Model2
nested.dne
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model3,
        data=data,
        bindings=snapshot([{"x": 1}, {"x": 2}, {"x": 3}]),
        exception_message=snapshot("""\
1 validation error for Model3
dne
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model4,
        data=data,
        bindings=snapshot(
            [{"nested": {"x": 1}}, {"nested": {"x": 2}}, {"nested": {"x": 3}}]
        ),
        exception_message=snapshot("""\
1 validation error for Model4
nested.dne
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model5,
        data=data,
        bindings=snapshot(
            [
                {"x": 1, "nested": {"x": 1}},
                {"x": 2, "nested": {"x": 2}},
                {"x": 3, "nested": {"x": 3}},
            ]
        ),
        exception_message=snapshot("""\
1 validation error for Model5
nested.dne
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model6,
        data=data,
        bindings=snapshot([{"x": 1}, {"x": 2}, {"x": 3}]),
        exception_message=snapshot("""\
1 validation error for Model6
ALIAS
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
    Parameter(
        model=Model7,
        data=data,
        bindings=snapshot(
            [{"nested": {"x": 1}}, {"nested": {"x": 2}}, {"nested": {"x": 3}}]
        ),
        exception_message=snapshot("""\
1 validation error for Model7
nested.ALIAS
  Field required [type=missing, input_value={'x': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing\
"""),
    ),
]


@pytest.mark.parametrize("param", params)
def test_sad_path_missing_field(param):
    """generate_bindings() never validates; generate_models() does and must
    raise with a message scoped to the offending (possibly nested/aliased) field.
    """

    materializer = ModelMaterializer(model=param.model, data=param.data)

    assert list(materializer.generate_bindings()) == param.bindings
    with pytest.raises(ValidationError) as exc_info:
        list(materializer.generate_models())
    assert str(exc_info.value) == param.exception_message
