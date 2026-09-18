from collections import UserDict
from functools import cached_property

from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import InvalidGroupByError
from graphty.utils.type_utils import is_structured_field_static_type
from pydantic import BaseModel


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁModelInfoǁ__init____mutmut: MutantDict = {}  # type: ignore


class ModelInfo[TModel: type[BaseModel]]:
    @_mutmut_mutated(mutants_xǁModelInfoǁ__init____mutmut)
    def __init__(self, model: TModel, base_cols: set[str]) -> None:
        self.model = model
        self.base_cols = base_cols
    def xǁModelInfoǁ__init____mutmut_orig(self, model: TModel, base_cols: set[str]) -> None:
        self.model = model
        self.base_cols = base_cols
    def xǁModelInfoǁ__init____mutmut_1(self, model: TModel, base_cols: set[str]) -> None:
        self.model = None
        self.base_cols = base_cols
    def xǁModelInfoǁ__init____mutmut_2(self, model: TModel, base_cols: set[str]) -> None:
        self.model = model
        self.base_cols = None

    @cached_property
    def alias_map(self) -> AliasMap:
        return AliasMap(model=self.model, projection=self.base_cols)

    @cached_property
    def model_projection(self) -> set[str]:
        return {
            self.alias_map[field_name]
            for field_name, field_info in self.model.model_fields.items()
            if not is_structured_field_static_type(field_info.annotation)
        }

    @cached_property
    def group_by(self) -> str | None:
        if (group_by := self.model.model_config.get("group_by")) is None:
            return None

        applicable_fields: set[str] = {
            field_name
            for field_name, field_info in self.model.model_fields.items()
            if not is_structured_field_static_type(field_info.annotation)
        }

        if group_by not in applicable_fields:
            raise InvalidGroupByError(group_by_value=group_by, model=self.model)

        return self.alias_map[group_by]

mutants_xǁModelInfoǁ__init____mutmut['_mutmut_orig'] = ModelInfo.xǁModelInfoǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelInfoǁ__init____mutmut['xǁModelInfoǁ__init____mutmut_1'] = ModelInfo.xǁModelInfoǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelInfoǁ__init____mutmut['xǁModelInfoǁ__init____mutmut_2'] = ModelInfo.xǁModelInfoǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelInfoRegistryǁ__missing____mutmut: MutantDict = {}  # type: ignore


class ModelInfoRegistry(UserDict[type[BaseModel], ModelInfo]):
    @_mutmut_mutated(mutants_xǁModelInfoRegistryǁ__init____mutmut)
    def __init__(self, base_cols: set[str]) -> None:
        self.base_cols = base_cols
        self.data: dict[type[BaseModel], ModelInfo] = {}
    def xǁModelInfoRegistryǁ__init____mutmut_orig(self, base_cols: set[str]) -> None:
        self.base_cols = base_cols
        self.data: dict[type[BaseModel], ModelInfo] = {}
    def xǁModelInfoRegistryǁ__init____mutmut_1(self, base_cols: set[str]) -> None:
        self.base_cols = None
        self.data: dict[type[BaseModel], ModelInfo] = {}
    def xǁModelInfoRegistryǁ__init____mutmut_2(self, base_cols: set[str]) -> None:
        self.base_cols = base_cols
        self.data: dict[type[BaseModel], ModelInfo] = None

    @_mutmut_mutated(mutants_xǁModelInfoRegistryǁ__missing____mutmut)
    def __missing__(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, base_cols=self.base_cols)
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_orig(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, base_cols=self.base_cols)
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_1(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = None
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_2(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=None, base_cols=self.base_cols)
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_3(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, base_cols=None)
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_4(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(base_cols=self.base_cols)
        return self[key]

    def xǁModelInfoRegistryǁ__missing____mutmut_5(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, )
        return self[key]

mutants_xǁModelInfoRegistryǁ__init____mutmut['_mutmut_orig'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__init____mutmut['xǁModelInfoRegistryǁ__init____mutmut_1'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__init____mutmut['xǁModelInfoRegistryǁ__init____mutmut_2'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁModelInfoRegistryǁ__missing____mutmut['_mutmut_orig'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__missing____mutmut['xǁModelInfoRegistryǁ__missing____mutmut_1'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__missing____mutmut['xǁModelInfoRegistryǁ__missing____mutmut_2'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__missing____mutmut['xǁModelInfoRegistryǁ__missing____mutmut_3'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__missing____mutmut['xǁModelInfoRegistryǁ__missing____mutmut_4'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelInfoRegistryǁ__missing____mutmut['xǁModelInfoRegistryǁ__missing____mutmut_5'] = ModelInfoRegistry.xǁModelInfoRegistryǁ__missing____mutmut_5 # type: ignore # mutmut generated
