import types
import typing
from typing import Annotated, TypeGuard, get_args, get_origin

from pydantic import BaseModel
from pydantic.fields import FieldInfo
from typing_extensions import TypeForm


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_de_annotate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_de_annotate__mutmut)
def de_annotate(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_orig(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_1(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(None) is Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_2(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is not Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_3(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = None
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_4(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = get_args(None)
        return de_annotate(type_form)
    return type_form


def x_de_annotate__mutmut_5(type_form: TypeForm) -> TypeForm:
    """Unwrap potentially nested Annotated wrappers."""

    if get_origin(type_form) is Annotated:
        type_form, *_ = get_args(type_form)
        return de_annotate(None)
    return type_form

mutants_x_de_annotate__mutmut['_mutmut_orig'] = x_de_annotate__mutmut_orig # type: ignore # mutmut generated
mutants_x_de_annotate__mutmut['x_de_annotate__mutmut_1'] = x_de_annotate__mutmut_1 # type: ignore # mutmut generated
mutants_x_de_annotate__mutmut['x_de_annotate__mutmut_2'] = x_de_annotate__mutmut_2 # type: ignore # mutmut generated
mutants_x_de_annotate__mutmut['x_de_annotate__mutmut_3'] = x_de_annotate__mutmut_3 # type: ignore # mutmut generated
mutants_x_de_annotate__mutmut['x_de_annotate__mutmut_4'] = x_de_annotate__mutmut_4 # type: ignore # mutmut generated
mutants_x_de_annotate__mutmut['x_de_annotate__mutmut_5'] = x_de_annotate__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_pydantic_model_static_type__mutmut)
def is_pydantic_model_static_type(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_orig(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_1(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = None

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_2(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(None)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_3(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel) or (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_4(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type) or issubclass(type_form, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_5(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(None, BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_6(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, None)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_7(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(BaseModel)
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_8(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, )
        and (type_form is not BaseModel)
    )


def x_is_pydantic_model_static_type__mutmut_9(type_form: TypeForm) -> TypeGuard[type[BaseModel]]:
    """Check if type_form denotes a Pydantic model type."""
    type_form = de_annotate(type_form)

    return (
        isinstance(type_form, type)
        and issubclass(type_form, BaseModel)
        and (type_form is BaseModel)
    )

mutants_x_is_pydantic_model_static_type__mutmut['_mutmut_orig'] = x_is_pydantic_model_static_type__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_1'] = x_is_pydantic_model_static_type__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_2'] = x_is_pydantic_model_static_type__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_3'] = x_is_pydantic_model_static_type__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_4'] = x_is_pydantic_model_static_type__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_5'] = x_is_pydantic_model_static_type__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_6'] = x_is_pydantic_model_static_type__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_7'] = x_is_pydantic_model_static_type__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_8'] = x_is_pydantic_model_static_type__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_static_type__mutmut['x_is_pydantic_model_static_type__mutmut_9'] = x_is_pydantic_model_static_type__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_parametrized_list_static_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_parametrized_list_static_type__mutmut)
def is_parametrized_list_static_type(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(type_form)
    return get_origin(type_form) is list


def x_is_parametrized_list_static_type__mutmut_orig(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(type_form)
    return get_origin(type_form) is list


def x_is_parametrized_list_static_type__mutmut_1(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = None
    return get_origin(type_form) is list


def x_is_parametrized_list_static_type__mutmut_2(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(None)
    return get_origin(type_form) is list


def x_is_parametrized_list_static_type__mutmut_3(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(type_form)
    return get_origin(None) is list


def x_is_parametrized_list_static_type__mutmut_4(type_form: TypeForm) -> TypeGuard[type[list]]:
    """Check if type_form denotes a parametrized list type."""
    type_form = de_annotate(type_form)
    return get_origin(type_form) is not list

mutants_x_is_parametrized_list_static_type__mutmut['_mutmut_orig'] = x_is_parametrized_list_static_type__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_parametrized_list_static_type__mutmut['x_is_parametrized_list_static_type__mutmut_1'] = x_is_parametrized_list_static_type__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_parametrized_list_static_type__mutmut['x_is_parametrized_list_static_type__mutmut_2'] = x_is_parametrized_list_static_type__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_parametrized_list_static_type__mutmut['x_is_parametrized_list_static_type__mutmut_3'] = x_is_parametrized_list_static_type__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_parametrized_list_static_type__mutmut['x_is_parametrized_list_static_type__mutmut_4'] = x_is_parametrized_list_static_type__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_pydantic_model_union_static_type__mutmut)
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


def x_is_pydantic_model_union_static_type__mutmut_orig(
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


def x_is_pydantic_model_union_static_type__mutmut_1(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = None

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_2(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(None)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_3(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = None
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_4(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(None) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_5(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) not in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_6(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = None

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_7(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        None
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_8(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) and is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_9(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(None) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_10(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(None)
        for obj in get_args(type_form)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_11(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(None)
    )

    return is_union_type and has_any_model


def x_is_pydantic_model_union_static_type__mutmut_12(
    type_form: TypeForm,
) -> TypeGuard[types.UnionType]:
    """Check if type_form denotes a union type of a Pydantic model."""

    type_form = de_annotate(type_form)

    is_union_type: bool = get_origin(type_form) in (types.UnionType, typing.Union)
    has_any_model: bool = any(
        is_pydantic_model_static_type(obj) or is_pydantic_model_union_static_type(obj)
        for obj in get_args(type_form)
    )

    return is_union_type or has_any_model

mutants_x_is_pydantic_model_union_static_type__mutmut['_mutmut_orig'] = x_is_pydantic_model_union_static_type__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_1'] = x_is_pydantic_model_union_static_type__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_2'] = x_is_pydantic_model_union_static_type__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_3'] = x_is_pydantic_model_union_static_type__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_4'] = x_is_pydantic_model_union_static_type__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_5'] = x_is_pydantic_model_union_static_type__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_6'] = x_is_pydantic_model_union_static_type__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_7'] = x_is_pydantic_model_union_static_type__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_8'] = x_is_pydantic_model_union_static_type__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_9'] = x_is_pydantic_model_union_static_type__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_10'] = x_is_pydantic_model_union_static_type__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_11'] = x_is_pydantic_model_union_static_type__mutmut_11 # type: ignore # mutmut generated
mutants_x_is_pydantic_model_union_static_type__mutmut['x_is_pydantic_model_union_static_type__mutmut_12'] = x_is_pydantic_model_union_static_type__mutmut_12 # type: ignore # mutmut generated
mutants_x_is_structured_field_static_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_structured_field_static_type__mutmut)
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


def x_is_structured_field_static_type__mutmut_orig(type_form: TypeForm) -> bool:
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


def x_is_structured_field_static_type__mutmut_1(type_form: TypeForm) -> bool:
    """Check if type_form denotes a structured field type.

    A structured field type is a type that triggers a recursion
    and/or aggregation code path in the GraphTy planner.
    """
    return any(
        None
    )


def x_is_structured_field_static_type__mutmut_2(type_form: TypeForm) -> bool:
    """Check if type_form denotes a structured field type.

    A structured field type is a type that triggers a recursion
    and/or aggregation code path in the GraphTy planner.
    """
    return any(
        predicate(None)
        for predicate in [
            is_pydantic_model_static_type,
            is_pydantic_model_union_static_type,
            is_parametrized_list_static_type,
        ]
    )

mutants_x_is_structured_field_static_type__mutmut['_mutmut_orig'] = x_is_structured_field_static_type__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_structured_field_static_type__mutmut['x_is_structured_field_static_type__mutmut_1'] = x_is_structured_field_static_type__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_structured_field_static_type__mutmut['x_is_structured_field_static_type__mutmut_2'] = x_is_structured_field_static_type__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_metadata__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_metadata__mutmut)
def get_metadata[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        (entry for entry in field_info.metadata if isinstance(entry, cls)),
        None,
    )


def x_get_metadata__mutmut_orig[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        (entry for entry in field_info.metadata if isinstance(entry, cls)),
        None,
    )


def x_get_metadata__mutmut_1[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        None,
        None,
    )


def x_get_metadata__mutmut_2[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        None,
    )


def x_get_metadata__mutmut_3[T](field_info: FieldInfo, cls: type[T]) -> T | None:
    """Generic typing.Annotated metadata lookup helper."""
    return next(
        (entry for entry in field_info.metadata if isinstance(entry, cls)),
        )

mutants_x_get_metadata__mutmut['_mutmut_orig'] = x_get_metadata__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_metadata__mutmut['x_get_metadata__mutmut_1'] = x_get_metadata__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_metadata__mutmut['x_get_metadata__mutmut_2'] = x_get_metadata__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_metadata__mutmut['x_get_metadata__mutmut_3'] = x_get_metadata__mutmut_3 # type: ignore # mutmut generated
