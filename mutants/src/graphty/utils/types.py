from pydantic import ConfigDict as PydanticConfigDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ConfigDict(PydanticConfigDict):
    group_by: str
