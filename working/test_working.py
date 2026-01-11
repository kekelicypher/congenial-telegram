import pytest
from working import convert


def test_1():
    assert (convert("9:00 AM to 5:00 PM") == "09:00 to 17:00")
    assert (convert("12:30 AM to 12:30 PM") == "12:30 to 00:30")


def test_2():
    assert (convert("9:00 AM to 5 PM") == "09:00 to 17:00")
    assert (convert("9 AM to 5:00 PM") == "09:00 to 17:00")
    assert (convert("9 AM to 5 PM") == "09:00 to 17:00")


def test_3():
    assert (convert("12 AM to 6 PM") == "12:00 to 18:00")
    assert (convert("12 AM to 3 AM") == "12:00 to 03:00")
