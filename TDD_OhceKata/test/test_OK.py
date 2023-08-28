import pytest
from app.OhceKata import *
def test_saludar_noche():
    assert saludar_noche("Pedro",20) == "¡Buenas noches Pedro!"
    assert saludar_noche("Ale",22) == "¡Buenas noches Ale!"

def test_saludar_tarde():
    assert saludar_tarde("Pedro",12) == "¡Buenas tardes Pedro!"
    assert saludar_tarde("Ale",18) == "¡Buenas tardes Ale!"

def test_saludar_dia():
    assert saludar_dia("Pedro",10) == "¡Buenos días Pedro!"
    assert saludar_dia("Ale",8) == "¡Buenos días Ale!"    
    
   