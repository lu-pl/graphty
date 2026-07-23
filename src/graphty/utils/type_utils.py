import types
import typing
from typing import Annotated, TypeGuard, get_args, get_origin

from pydantic import BaseModel
from pydantic.fields import FieldInfo
from typing_extensions import TypeForm


def de_annotate(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(type_form)
    return type_form


def is_pydantic_model_static_type(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def is_parametrized_list_static_type(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(type_form)
    return get_origin(type_form) is list


def is_pydantic_model_union_static_type(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def is_structured_field_static_type(type_form: TypeForm) -> bool:
    """Check if type_form denotes a structured field type.

    A structured field type is a type that triggers a recursion
    and/or aggregation code path in the GraphTy planner.
    """
    return any(
        predicate(type_form)
        for predicate in [
            is_pydantic_model_static_type,
            is_pydantic_model_union_static_type,
            is_parametrized_list_static_type,
        ]
    )


def get_metadata[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        (entry for entry in field_info.metadata if isinstance(entry, cls)),
        None,
    )
