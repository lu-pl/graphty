from collections import UserDict
from functools import cached_property

from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import InvalidGroupByError
from graphty.utils.type_utils import get_metadata, is_structured_field_static_type
from graphty.utils.types import Opaque
from pydantic import BaseModel


class ModelInfo[TModel: type[BaseModel]]:
    def __init__(self, model: TModel, base_cols: set[str]) -> None:
        self.model = model
        self.base_cols = base_cols

    @cached_property
    def alias_map(self) -> AliasMap:
        return AliasMap(model=self.model, projection=self.base_cols)

    @cached_property
    def model_projection(self) -> set[str]:
        return {
            self.alias_map[field_name]
            for field_name, field_info in self.model.model_fields.items()
            if not is_structured_field_static_type(field_info.annotation)
            and not get_metadata(field_info=field_info, cls=Opaque)
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


class ModelInfoRegistry(UserDict[type[BaseModel], ModelInfo]):
    def __init__(self, base_cols: set[str]) -> None:
        self.base_cols = base_cols
        self.data: dict[type[BaseModel], ModelInfo] = {}

    def __missing__(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, base_cols=self.base_cols)
        return self[key]
