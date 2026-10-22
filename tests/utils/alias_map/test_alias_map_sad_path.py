from dataclasses import dataclass

import pytest
from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import AliasResolutionError
from pydantic import AliasChoices, AliasPath, BaseModel, ConfigDict, Field


class Model1(BaseModel):
    x: int = Field(alias=AliasChoices("a", "b"))


class Model2(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class Model3(BaseModel):
    x: int = Field(alias=AliasPath(""))


class Model4(BaseModel):
    x: int = Field(alias=AliasChoices("a", AliasPath("")))


@dataclass
class Parameter:
    model: object
    projection: object
    exception: type[Exception]
    match: str


params: list[Parameter] = [
    # AliasChoice/projection mismatch: empty projection.
    Parameter(
        model=Model1,
        projection=set(),
        exception=AliasResolutionError,
        match="Empty or missing input data projection.",
    ),
    # AliasChoice/projection mismatch: projection doesn't contain any computed
    # alias.
    Parameter(
        model=Model1,
        projection={"x", "y", "z"},
        exception=AliasResolutionError,
        match="None of computed aliases .* in input data projection",
    ),
    # `populate_by_name` config is no longer supported, superseded by Pydantic's
    # validate_by_name/validate_by_alias flags.
    Parameter(
        model=Model2,
        projection=set(),
        exception=ValueError,
        match=(
            "Config option 'populate_by_name' is not supported. "
            "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
        ),
    ),
    Parameter(
        model=Model3,
        projection=set(),
        exception=NotImplementedError,
        match="Unable to resolve alias. Expected str or AliasChoices of str",
    ),
    Parameter(
        model=Model4,
        projection=set(),
        exception=NotImplementedError,
        match="Unable to resolve alias. Expected str or AliasChoices of str",
    ),
]


@pytest.mark.parametrize("param", params)
def test_alias_map_sad_path(param):
    with pytest.raises(param.exception, match=param.match):
        AliasMap(model=param.model, projection=param.projection)
