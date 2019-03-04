import pytest


@pytest.fixture(scope='class', autouse=True)
def my_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mytmpdir')
    a_file = a_dir.join('tmpfile.txt')
    text = 'hello, pytest!'

    a_file.write(text)

    return a_file


class TestTmpdirFactory(object):

    def test_001(self):
        pass

    def test_002(self):
        pass
