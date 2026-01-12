import pytest

from plates import is_valid


def test_first():
    assert is_valid("ABC432") == True


def test_second():
    assert is_valid("ABC043") == False


def test_third():
    assert is_valid("ABC123456") == False
    assert is_valid("ABC")


def test_fourth():
    assert is_valid("AV,C100") == False
