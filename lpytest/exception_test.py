# 如期抛出预期的异常

import pytest


def test_raises():
    type_error_wording = 'W'

    with pytest.raises(TypeError) as e:
        raise TypeError(type_error_wording)

    assert e.value.args[0] == type_error_wording


@pytest.mark.xfail(reason='No exception')
def test_raises_none():
    type_error_wording = 'W'

    with pytest.raises(TypeError) as e:
        pass
