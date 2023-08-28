import pytest
from app.OhceKata import *
def test_saludar_noche():
    assert saludar_noche("Pedro") == "¡Buenas noches Pedro!"

def test_saludar_tarde():
    assert saludar_tarde("Pedro") == "¡Buenas tardes Pedro!"

def test_saludar_dia():
    assert saludar_dia("Pedro") == "¡Buenos días Pedro!"