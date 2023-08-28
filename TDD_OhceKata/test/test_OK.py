import pytest
from app.OhceKata import *
def test_saludar_noche():
    assert saludar_noche("Pedro") == "¡Buenas noches Pedro!"