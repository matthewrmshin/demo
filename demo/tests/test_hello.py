import sys

from ..hello import get_hello, main


def test_get_hello():
    assert get_hello() == 'Hello World!'
    assert get_hello('Kitty') == 'Hello Kitty!'


def test_main(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['', ''])
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Hello World!\n'
