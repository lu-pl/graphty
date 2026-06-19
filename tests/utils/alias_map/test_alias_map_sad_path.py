import pytest
from graphty.utils.alias_map import AliasMap
from tests.utils.alias_map.parameters_sad_path import params_sad_path


@pytest.mark.parametrize("param", params_sad_path)
def test_alias_map_sad_path(param):
    with pytest.raises(param.expected.exception, match=param.expected.match):
        AliasMap(**param.kwargs)
