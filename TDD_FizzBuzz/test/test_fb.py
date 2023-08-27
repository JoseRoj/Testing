import pytest
from app.fizzbuzz import fizz_buzz

def test_normal():
    for i in [1, 2, 4, 7]:
        assert fizz_buzz(i) == i

