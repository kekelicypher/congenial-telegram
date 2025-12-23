import pytest

from bank import value


def test_hello():
    assert (value("hello, how is it going?") == 0)


def test_h():
    assert (value("hi, mate?") == 20)


def test_none():
    assert (value("What's up, man?") == 100)
