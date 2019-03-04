import pytest


class Test():
    """
    pytest -m "finished or unfinished"  mark_run_test.py
    pytest -m "not unfinished"  mark_run_test.py
    """

    @pytest.mark.finished
    def test_func1(self):
        assert 1 == 1

    @pytest.mark.xfail(reason='Not finished')
    @pytest.mark.unfinished
    def test_func2(self):
        assert 1 != 1
