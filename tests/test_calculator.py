"""
test_calculator.py

Tests basic arithmetic operations.

"""
from linuxforhealth.packaging.calculator import add, subtract
import pytest


@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (10, 20, 30),
    (15, 12, 27),
    (100, 300, 400)
])
def test_add(a, b, result):
    r = add(a, b)
    assert r == result


@pytest.mark.parametrize("a,b,result", [
    (1, 2, -1),
    (10, 20, -10),
    (15, 12, 3),
    (100, 300, -200)
])
def test_subtract(a, b, result):
    r = subtract(a, b)
    assert r == result
