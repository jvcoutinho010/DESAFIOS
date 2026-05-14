"""Testes automatizados para o módulo calculadora.

Cobre os casos normais, extremos e de erro de cada função,
seguindo as boas práticas da Aula 1.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from meu_projeto.utils.calculadora import dividir, multiplicar, somar, subtrair


# ── multiplicar ───────────────────────────────────────────────────────────────

class TestMultiplicar:
    """Testes para a função multiplicar."""

    def test_resultado_positivo(self):
        assert multiplicar(4, 5) == 20

    def test_com_zero(self):
        assert multiplicar(0, 99) == 0

    def test_numeros_negativos(self):
        assert multiplicar(-3, 4) == -12

    def test_dois_negativos(self):
        assert multiplicar(-3, -3) == 9

    def test_float(self):
        assert multiplicar(2.5, 4) == pytest.approx(10.0)


# ── somar ─────────────────────────────────────────────────────────────────────

class TestSomar:
    """Testes para a função somar."""

    def test_soma_basica(self):
        assert somar(3, 7) == 10

    def test_com_negativo(self):
        assert somar(-5, 3) == -2

    def test_soma_zero(self):
        assert somar(0, 0) == 0

    def test_float(self):
        assert somar(1.1, 2.2) == pytest.approx(3.3)


# ── subtrair ──────────────────────────────────────────────────────────────────

class TestSubtrair:
    """Testes para a função subtrair."""

    def test_subtracao_basica(self):
        assert subtrair(10, 3) == 7

    def test_resultado_negativo(self):
        assert subtrair(3, 10) == -7

    def test_com_zero(self):
        assert subtrair(5, 0) == 5


# ── dividir ───────────────────────────────────────────────────────────────────

class TestDividir:
    """Testes para a função dividir."""

    def test_divisao_exata(self):
        assert dividir(10, 2) == 5.0

    def test_divisao_com_decimal(self):
        assert dividir(7, 2) == pytest.approx(3.5)

    def test_divisao_por_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="zero"):
            dividir(10, 0)

    def test_negativos(self):
        assert dividir(-10, 2) == -5.0
