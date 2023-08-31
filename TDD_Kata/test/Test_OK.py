import pytest 
from app.Ohce import *

def test_saludar_noche():
    assert saludar("Pedro",20) == "¡Buenas noches Pedro!"
    assert saludar("Kel",3) == "¡Buenas noches Kel!"
    assert saludar("Juan",5) == "¡Buenas noches Juan!"
