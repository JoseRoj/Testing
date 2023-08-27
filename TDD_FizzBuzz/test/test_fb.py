import pytest
from app.fizzbuzz import fizz_buzz

def test_normal():
    assert fizz_buzz(1) == 1