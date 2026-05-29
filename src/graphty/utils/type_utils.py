import types
import typing
from typing import Annotated, TypeGuard, get_args, get_origin

from pydantic import BaseModel
from typing_extensions import TypeForm


def is_list_static_type(obj: TypeForm) -> TypeGuard[type[list]]:
    """Check if object is a list type."""
    return (obj is list) or (get_origin(obj) is list)


def is_pydantic_model_static_type(obj: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if object is a Pydantic model type."""
    if get_origin(obj) is Annotated:
        obj, *_ = get_args(obj)

    return (
        isinstance(obj, type) and issubclass(obj, BaseModel) and (obj is not BaseModel)
    )


def is_list_pydantic_model_static_type(
    obj: TypeForm,
) -> TypeGuard[type[list[type[BaseModel]]]]:
    """Check if an object is a list of Pydantic models type."""
    return is_list_static_type(obj) and all(
        is_pydantic_model_static_type(t) for t in get_args(obj)
    )


def is_pydantic_model_union_static_type(
    obj: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if object is a union type of a Pydantic model."""
    if get_origin(obj) is Annotated:
        obj, *_ = get_args(obj)

    is_union_type: bool = get_origin(obj) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) for obj in get_args(obj)
    )

    return is_union_type and has_any_model
