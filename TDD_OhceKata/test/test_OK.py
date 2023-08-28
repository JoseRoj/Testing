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
    assert isPalindrome("ana", "Pedro")[0] == "ana"
    assert isPalindrome("ana", "Pedro")[1] == "¡Bonita palabra!"
    assert isPalindrome("anita lava la tina", "Pedro")[0] == "anit al aval atina"
    assert isPalindrome("anita lava la tina", "Pedro")[1] == "¡Bonita palabra!"
    assert isPalindrome("hola", "Pedro") == "aloh"
    assert isPalindrome("Stop!", "Pedro") == "Adios Pedro"
   