# Racheal && Josephine

from fibonnaci import fib
import pytest


# this test failed on the first test attempt
# then test it passed on next attempt
def test_fib0_returns_0():
    assert fib(0) == 0


# this failed before i had updated
def test_fib1_returns_0():
    assert fib(1) == 1


# this failed before i had updated
def test_fib1_returns_2():
    assert fib(2) == 1


def test_fib1_returns_3():
    assert fib(3) == 2


def test_fib1_returns_4():
    assert fib(4) == 3


def test_fib1_returns_5():
    assert fib(5) == 5


def test_fib1_returns_6():
    assert fib(6) == 8


def test_fib1_negative_number_returns_error():
    with pytest.raises(ValueError):
        fib(-3)

def test_fib1_not_integer_returns_error():
    with pytest.raises(TypeError):
        fib(5.0)
