import pytest
from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert (jar.size <= jar.capacity) == True
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
