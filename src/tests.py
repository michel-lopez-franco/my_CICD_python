from main import Calculadora
import pandas as pd


def test_sums_2_numbers():
    assert Calculadora.suma(2, 3) == 5
