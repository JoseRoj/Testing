import pytest
from app.fizzbuzz import fizz_buzz

def test_normal():
    for i in [1, 2, 4, 7]:
        assert fizz_buzz(i) == i

def test_mult3():
    assert fizz_buzz(3) == "fizz"
    assert fizz_buzz(6) == "fizz"  
    assert fizz_buzz(9) == "fizz"