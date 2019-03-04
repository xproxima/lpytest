import pytest


@pytest.mark.xfail(1 < 2, reason="not supported until 2.0")
def test_expect_fail_if_true():
    assert 2 == 1


@pytest.mark.xfail(reason="not supported until 2.0")
def test_expect_fail():
    assert 2 == 1


@pytest.mark.xfail(1 == 2, reason="not supported until 2.0")
def test_expect_fail_if_false():
    assert 2 == 1


@pytest.mark.xfail(reason="not supported until 2.0")
def test_expect_fail_succ():
    assert 2 == 2
