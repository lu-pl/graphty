from pydantic import ConfigDict as PydanticConfigDict


class ConfigDict(PydanticConfigDict):
    group_by: str
