import pytest 
from app.Ohce import *

def test_saludar_noche():
    assert saludar("Pedro") == "¡Buenas noches Pedro!"
