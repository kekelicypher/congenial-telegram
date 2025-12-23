import pytest

from twttr import shorten


def test_lower():
    assert(shorten("twitter") == "twttr")

def test_upper():
    assert(shorten("Emmanuel") == "mmnl")
    assert(shorten("NEWT") == "NWT")