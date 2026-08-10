from typing import NamedTuple

from pydantic import AliasChoices, AliasPath, BaseModel, ConfigDict, Field


class RaisesParameter(NamedTuple):
    exception: type[Exception]
    match: str | None = None


class TestParameter(NamedTuple):
    kwargs: dict[str, object]
    expected: RaisesParameter
    description: str | None = None


class Model1(BaseModel):
    x: int = Field(alias=AliasChoices("a", "b"))


class Model2(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class Model3(BaseModel):
    x: int = Field(alias=AliasPath(""))


class Model4(BaseModel):
    x: int = Field(alias=AliasChoices("a", AliasPath("")))


params_sad_path: list[TestParameter] = [
    TestParameter(
        description="""Test case for checking that a ValueError
        is raised for AliasChoice/projection mismatches.""",
        kwargs={"model": Model1, "projection": set()},
        expected=RaisesParameter(
            exception=ValueError, match="Unable to resolve AliasChoice"
        ),
    ),
    TestParameter(
        description="""Test case for checking that a ValueError
        is raised for AliasChoice/projection mismatches.""",
        kwargs={"model": Model1, "projection": {"x", "y", "z"}},
        expected=RaisesParameter(
            exception=ValueError, match="Unable to resolve AliasChoice"
        ),
    ),
    TestParameter(
        description="Test case for checking that `populate_by_name` config raises.",
        kwargs={"model": Model2, "projection": set()},
        expected=RaisesParameter(
            exception=ValueError,
            match=(
                "Config option 'populate_by_name' is not supported. "
                "Use Pydantic >=2.11 flags 'validate_by_name'/'validate_by_alias' instead."
            ),
        ),
    ),
    TestParameter(
        kwargs={"model": Model3, "projection": set()},
        expected=RaisesParameter(
            exception=NotImplementedError,
            match="Unable to resolve alias. Expected str or AliasChoices of str",
        ),
    ),
    TestParameter(
        kwargs={"model": Model4, "projection": set()},
        expected=RaisesParameter(
            exception=NotImplementedError,
            match="Unable to resolve alias. Expected str or AliasChoices of str",
        ),
    ),
]
