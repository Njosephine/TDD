# Pair: Nanyonga Josephine && Racheal Abaasa

from factorial import factorial
import pytest


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_five():
    assert factorial(5) == 120


def test_factorial_seven():
    assert factorial(7) == 5040


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-4)
