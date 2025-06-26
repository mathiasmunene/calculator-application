import pytest
from lib.calculator import sum, minus, multiply, divide

def test_sum():
    assert sum(100, 1) == 101
def test_minus():
    assert minus(100, 1) == 99
def test_multiply():
    assert multiply(3, 20) == 60
def test_divide():
    assert divide(27,3) == 9
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)