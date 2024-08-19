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
    assert isPalindrome("Anita lava la tina") == "¡Bonita palabra!"
    
def test_saludo_adios():
    assert saludo_adios("Pedro", 20) == "¡Buenas noches Pedro!\n¡Adios Pedro!"
    assert saludo_adios("Juan", 12) == "¡Buenas tardes Juan!\n¡Adios Juan!"
    assert saludo_adios("Ale", 8) == "¡Buenos días Ale!\n¡Adios Ale!"
    
def test_all():
    assert all("Pedro",20,["ana","stop","oto","Stop!"]) == "¡Buenas noches Pedro!\nana\n¡Bonita palabra!\npots\noto\n¡Bonita palabra!\nAdios Pedro"
    assert all("Leo",12,["Juan","stop","Somos o no somos","Stop!"]) == "¡Buenas tardes Leo!\nnauJ\npots\nsomos on o somoS\n¡Bonita palabra!\nAdios Leo"