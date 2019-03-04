import pytest


@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.skip(reason='out-of-date api')
def test_func2():
    assert 1 != 1


@pytest.mark.skipif(2 > 1, reason='not supported until 2')
def test_func3():
    assert 1 != 1


@pytest.mark.xfail(reason='skipif failed')
@pytest.mark.skipif(2 < 1, reason='not supported until 2')
def test_func4():
    assert 1 != 1
