import os
import json


def dump_config(config):
    path = os.path.expanduser('~/.conf.json')
    with open(path, 'w', encoding='utf-8') as wr:
        json.dump(config, wr, indent=4)


def test_config_monkeypatch2(tmpdir, monkeypatch):
    config = {'1': 2}
    fake_home = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'expanduser',
                        lambda x: x.replace('~', str(fake_home)))
    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config


def test_config_monkeypatch(tmpdir_factory, monkeypatch):
    config = {'1': 2}
    fake_home = tmpdir_factory.mktemp('home')
    monkeypatch.setattr(os.path, 'expanduser',
                        lambda x: x.replace('~', str(fake_home)))
    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config
