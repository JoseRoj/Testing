import pytest
from app.fizzbuzz import fizz_buzz

def test_normal():
    for i in [1, 2, 4, 7]:
        assert fizz_buzz(i) == i

def test_mult3():
    for i in [3, 6, 9]:
        assert fizz_buzz(i) == "fizz"

def test_mult5():
    for i in [5, 10]:
        assert fizz_buzz(i) == "buzz"