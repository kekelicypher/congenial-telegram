import pytest
from numb3rs import validate


def test_1():
    assert (validate("1.1.1.1") == True)
    assert (validate(".1.1.1") == False)
    assert (validate("1.1.1.1") == True)


def test_2():
    assert (validate("101.1.1") == False)
    assert (validate("11.1.1") == False)
    assert (validate("25") == False)
    assert (validate("250.20") == False)


def test_3():
    assert (validate("275.1.65.8") == False)
    assert (validate("255.255.255.255") == True)
    assert (validate("000.00.0.0") == False)
