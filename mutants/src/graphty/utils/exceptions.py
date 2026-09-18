from pydantic import BaseModel
from typing_extensions import TypeForm


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMissingGroupByErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class MissingGroupByError(Exception):
    @_mutmut_mutated(mutants_xǁMissingGroupByErrorǁ__init____mutmut)
    def __init__(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "does not specify ConfigDict.group_by."
        )
    def xǁMissingGroupByErrorǁ__init____mutmut_orig(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "does not specify ConfigDict.group_by."
        )
    def xǁMissingGroupByErrorǁ__init____mutmut_1(self, model: type[BaseModel]) -> None:
        super().__init__(
            None
        )
    def xǁMissingGroupByErrorǁ__init____mutmut_2(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "XXdoes not specify ConfigDict.group_by.XX"
        )
    def xǁMissingGroupByErrorǁ__init____mutmut_3(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "does not specify configdict.group_by."
        )
    def xǁMissingGroupByErrorǁ__init____mutmut_4(self, model: type[BaseModel]) -> None:
        super().__init__(
            f"Model '{model.__name__}' with aggregation target "
            "DOES NOT SPECIFY CONFIGDICT.GROUP_BY."
        )

mutants_xǁMissingGroupByErrorǁ__init____mutmut['_mutmut_orig'] = MissingGroupByError.xǁMissingGroupByErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMissingGroupByErrorǁ__init____mutmut['xǁMissingGroupByErrorǁ__init____mutmut_1'] = MissingGroupByError.xǁMissingGroupByErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMissingGroupByErrorǁ__init____mutmut['xǁMissingGroupByErrorǁ__init____mutmut_2'] = MissingGroupByError.xǁMissingGroupByErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMissingGroupByErrorǁ__init____mutmut['xǁMissingGroupByErrorǁ__init____mutmut_3'] = MissingGroupByError.xǁMissingGroupByErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMissingGroupByErrorǁ__init____mutmut['xǁMissingGroupByErrorǁ__init____mutmut_4'] = MissingGroupByError.xǁMissingGroupByErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁInvalidGroupByErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class InvalidGroupByError(Exception):
    @_mutmut_mutated(mutants_xǁInvalidGroupByErrorǁ__init____mutmut)
    def __init__(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "Grouping keys must reference scalar model fields."
        )
    def xǁInvalidGroupByErrorǁ__init____mutmut_orig(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "Grouping keys must reference scalar model fields."
        )
    def xǁInvalidGroupByErrorǁ__init____mutmut_1(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            None
        )
    def xǁInvalidGroupByErrorǁ__init____mutmut_2(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "XXGrouping keys must reference scalar model fields.XX"
        )
    def xǁInvalidGroupByErrorǁ__init____mutmut_3(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "grouping keys must reference scalar model fields."
        )
    def xǁInvalidGroupByErrorǁ__init____mutmut_4(self, model: type[BaseModel], group_by_value: str) -> None:
        super().__init__(
            f"Invalid grouping key '{group_by_value}' for '{model.__name__}'. "
            "GROUPING KEYS MUST REFERENCE SCALAR MODEL FIELDS."
        )

mutants_xǁInvalidGroupByErrorǁ__init____mutmut['_mutmut_orig'] = InvalidGroupByError.xǁInvalidGroupByErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁInvalidGroupByErrorǁ__init____mutmut['xǁInvalidGroupByErrorǁ__init____mutmut_1'] = InvalidGroupByError.xǁInvalidGroupByErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁInvalidGroupByErrorǁ__init____mutmut['xǁInvalidGroupByErrorǁ__init____mutmut_2'] = InvalidGroupByError.xǁInvalidGroupByErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁInvalidGroupByErrorǁ__init____mutmut['xǁInvalidGroupByErrorǁ__init____mutmut_3'] = InvalidGroupByError.xǁInvalidGroupByErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁInvalidGroupByErrorǁ__init____mutmut['xǁInvalidGroupByErrorǁ__init____mutmut_4'] = InvalidGroupByError.xǁInvalidGroupByErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class MissingDiscriminatorError(Exception):
    @_mutmut_mutated(mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut)
    def __init__(self, type_form: TypeForm) -> None:
        super().__init__(
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )
    def xǁMissingDiscriminatorErrorǁ__init____mutmut_orig(self, type_form: TypeForm) -> None:
        super().__init__(
            "Multi-Model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )
    def xǁMissingDiscriminatorErrorǁ__init____mutmut_1(self, type_form: TypeForm) -> None:
        super().__init__(
            None
        )
    def xǁMissingDiscriminatorErrorǁ__init____mutmut_2(self, type_form: TypeForm) -> None:
        super().__init__(
            "XXMulti-Model unions must be discriminated unions. XX"
            f"Unable to extract discriminator for union type '{type_form}'."
        )
    def xǁMissingDiscriminatorErrorǁ__init____mutmut_3(self, type_form: TypeForm) -> None:
        super().__init__(
            "multi-model unions must be discriminated unions. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )
    def xǁMissingDiscriminatorErrorǁ__init____mutmut_4(self, type_form: TypeForm) -> None:
        super().__init__(
            "MULTI-MODEL UNIONS MUST BE DISCRIMINATED UNIONS. "
            f"Unable to extract discriminator for union type '{type_form}'."
        )

mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut['_mutmut_orig'] = MissingDiscriminatorError.xǁMissingDiscriminatorErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut['xǁMissingDiscriminatorErrorǁ__init____mutmut_1'] = MissingDiscriminatorError.xǁMissingDiscriminatorErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut['xǁMissingDiscriminatorErrorǁ__init____mutmut_2'] = MissingDiscriminatorError.xǁMissingDiscriminatorErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut['xǁMissingDiscriminatorErrorǁ__init____mutmut_3'] = MissingDiscriminatorError.xǁMissingDiscriminatorErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMissingDiscriminatorErrorǁ__init____mutmut['xǁMissingDiscriminatorErrorǁ__init____mutmut_4'] = MissingDiscriminatorError.xǁMissingDiscriminatorErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class AliasResolutionError(Exception):
    @_mutmut_mutated(mutants_xǁAliasResolutionErrorǁ__init____mutmut)
    def __init__(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "Empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_orig(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "Empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_1(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = None
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_2(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if (projection) and False
            else "Empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_3(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if (projection) or True
            else "Empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_4(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "XXEmpty or missing input data projection.XX"
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_5(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "empty or missing input data projection."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_6(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "EMPTY OR MISSING INPUT DATA PROJECTION."
        )
        super().__init__(
            f"Unable to resolve AliasChoice for field '{field_name}' "
            f"of model '{model.__name__}': {reason}"
        )
    def xǁAliasResolutionErrorǁ__init____mutmut_7(
        self,
        field_name: str,
        model: type[BaseModel],
        aliases: list[str],
        projection: set[str],
    ) -> None:
        reason = (
            f"None of computed aliases '{aliases}' "
            f"in input data projection '{projection}'."
            if projection
            else "Empty or missing input data projection."
        )
        super().__init__(
            None
        )

mutants_xǁAliasResolutionErrorǁ__init____mutmut['_mutmut_orig'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_1'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_2'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_3'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_4'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_5'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_6'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁAliasResolutionErrorǁ__init____mutmut['xǁAliasResolutionErrorǁ__init____mutmut_7'] = AliasResolutionError.xǁAliasResolutionErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
