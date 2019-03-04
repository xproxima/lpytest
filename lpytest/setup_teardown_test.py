import pytest
# pytest --setup-show setup_teardown_test.py


def setup_module(module):
    pass


def setup_function(function):
    pass


class Test_C1(object):

    def setup_class(cls):
        cls.x = 'y'

    def setup_method(self):
        self.y = 'yy'

    def test_001(self):
        assert self.x == 'y'
        assert self.y == 'yy'

    def test_002(self):
        assert self.x == 'y'
        assert self.y == 'yy'
