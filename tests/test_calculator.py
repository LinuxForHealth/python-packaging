from linuxforhealth.packaging.calculator import add
import pytest


@pytest.mark.parametrize("a,b,result",[
    (1, 2, 3),
    (10, 20, 30),
    (15, 12, 27),
    (100, 300, 400)
])
def test_add(a, b, result):
    r = add(a, b)
    assert r == result
