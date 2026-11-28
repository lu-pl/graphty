from collections import UserDict
from functools import cached_property

from pydantic import BaseModel

from graphty.utils.alias_map import AliasMap
from graphty.utils.exceptions import GroupByColumnNotFoundError, InvalidGroupByError
from graphty.utils.type_utils import is_structured_field_static_type


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

        group_by_column: str = self.alias_map[group_by]

        # Unlike absent value columns, absent grouping columns cannot be forwarded to Pydantic;
        # also, a default value on a grouping key field cannot meaningfully partition rows.
        if group_by_column not in self.base_cols:
            raise GroupByColumnNotFoundError(
                model=self.model,
                group_by_value=group_by,
                group_by_column=group_by_column,
                projection=self.base_cols,
            )

        return group_by_column


class ModelInfoRegistry(UserDict[type[BaseModel], ModelInfo]):
    def __init__(self, base_cols: set[str]) -> None:
        self.base_cols = base_cols
        self.data: dict[type[BaseModel], ModelInfo] = {}

    def __missing__(self, key: type[BaseModel]) -> ModelInfo:
        self.data[key] = ModelInfo(model=key, base_cols=self.base_cols)
        return self[key]
