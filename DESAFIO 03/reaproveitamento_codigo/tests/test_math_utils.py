import os
import sys
import time

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from utils.math_utils import cubo, medir_tempo, quadrado, raiz_quadrada


class TestCubo:
    """Testes para a função cubo."""

    def test_cubo_inteiro_positivo(self):
        assert cubo(2) == 8

    def test_cubo_tres(self):
        assert cubo(3) == 27

    def test_cubo_zero(self):
        assert cubo(0) == 0

    def test_cubo_negativo(self):
        assert cubo(-2) == -8

    def test_cubo_float(self):
        assert cubo(2.5) == pytest.approx(15.625)

    def test_cubo_um(self):
        assert cubo(1) == 1


class TestQuadrado:
   
    def test_quadrado_positivo(self):
        assert quadrado(4) == 16

    def test_quadrado_zero(self):
        assert quadrado(0) == 0

    def test_quadrado_negativo_vira_positivo(self):
        assert quadrado(-3) == 9

    def test_quadrado_float(self):
        assert quadrado(1.5) == pytest.approx(2.25)


class TestRaizQuadrada:
    
    def test_raiz_nove(self):
        assert raiz_quadrada(9) == pytest.approx(3.0)

    def test_raiz_zero(self):
        assert raiz_quadrada(0) == 0.0

    def test_raiz_negativo_levanta_erro(self):
        with pytest.raises(ValueError, match="negativo"):
            raiz_quadrada(-4)

    def test_raiz_float(self):
        assert raiz_quadrada(2) == pytest.approx(1.4142, rel=1e-3)


class TestMedirTempo:
  
    def test_preserva_resultado(self):
        @medir_tempo
        def dobrar(x):
            return x * 2

        assert dobrar(5) == 10

    def test_preserva_nome_da_funcao(self):
        @medir_tempo
        def minha_funcao():
            pass

        assert minha_funcao.__name__ == "minha_funcao"

    def test_funcao_lenta_registra_tempo(self):
        @medir_tempo
        def esperar():
            time.sleep(0.05)

        inicio = time.perf_counter()
        esperar()
        duracao = time.perf_counter() - inicio
        assert duracao >= 0.05
