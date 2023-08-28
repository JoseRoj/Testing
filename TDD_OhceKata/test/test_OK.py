import pytest
from app.OhceKata import *

def test_saludar():
    assert saludar("Pedro",20) == "¡Buenas noches Pedro!"
    assert saludar("Ale",22) == "¡Buenas noches Ale!"
    assert saludar("Pedro",12) == "¡Buenas tardes Pedro!"
    assert saludar("Ale",18) == "¡Buenas tardes Ale!"
    assert saludar("Pedro",10) == "¡Buenos días Pedro!"
    assert saludar("Ale",8) == "¡Buenos días Ale!"    
    
def test_palindrome():
    assert isPalindrome("ana")[0] == "ana"
    assert isPalindrome("ana")[1] == "¡Bonita palabra!"


   