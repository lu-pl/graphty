import pytest
from graphty.utils.alias_map import AliasMap
from tests.utils.alias_map.parameters import params


@pytest.mark.parametrize("param", params)
def test_alias_map(param):
    alias_map = AliasMap(**param.kwargs)
    assert alias_map == param.expected
