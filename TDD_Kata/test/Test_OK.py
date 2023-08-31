import pytest 
from app.Ohce import *

def test_saludar_noche():
    assert saludar("Pedro",20) == "¡Buenas noches Pedro!"
    assert saludar("Kel",3) == "¡Buenas noches Kel!"
    assert saludar("Juan",5) == "¡Buenas noches Juan!"

def test_saludar_dia():
    assert saludar("Pedro",7) == "¡Buenos días Pedro!"
    assert saludar("Ale",9) == "¡Buenos días Ale!"
    assert saludar("Juan",11) == "¡Buenos días Juan!"

def test_saludar_tarde():
    assert saludar("Pedro",12) == "¡Buenas tardes Pedro!"
    assert saludar("Ale",15) == "¡Buenas tardes Ale!"
    assert saludar("Juan",19) == "¡Buenas tardes Juan!"

def test_reverse():
    assert reverse("ana") == "ana"
    assert reverse("stop") == "pots"
    assert reverse("hola") == "aloh"
    
def test_isPalindrome():
    assert isPalindrome("ana") == "¡Bonita palabra!"
    assert isPalindrome("oto") == "¡Bonita palabra!"
    assert isPalindrome("hola") == ""
    