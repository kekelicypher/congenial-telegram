import pytest
from working import convert


def test_1():
    assert (convert("9:00 AM to 5:00 PM") == "09:00 to 17:00")
    assert (convert("12:60 AM, 13:00 PM") == False)


def test_2():
    assert (convert("9:00 AM to 5 PM") == "09:00 to 17:00")
    assert (convert("9 AM to 5:00 PM") == "09:00 to 17:00")
    assert (convert("9 AM to 5 PM") == "09:00 to 17:00")


def test_3():
    assert (convert("12 AM to 6 PM") == "00:00 to 18:00")
    assert (convert("12 AM to 3 AM") == "00:00 to 03:00")
