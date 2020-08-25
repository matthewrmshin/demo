import sys

from ..hello import main


def test_main(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['', ''])
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Hello World!\n'

    monkeypatch.setattr(sys, 'argv', ['', 'Kitty'])
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Hello Kitty!\n'
