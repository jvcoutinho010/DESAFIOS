import sys
import os
import pytest

# Garante que src/ seja encontrado ao rodar pytest na raiz do projeto
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from folha_pagamento.utils.calculos import (
    calcular_salario_clt,
    calcular_salario_estagiario,
    calcular_salario_freelancer,
)

class TestEstagiario:

    def test_salario_liquido_igual_ao_bruto(self):
        resultado = calcular_salario_estagiario(1500.0)
        assert resultado["salario_liquido"] == 1500.0

    def test_sem_desconto_inss(self):
        resultado = calcular_salario_estagiario(1500.0)
        assert resultado["desconto_inss"] == 0.0

    def test_sem_desconto_irrf(self):
        resultado = calcular_salario_estagiario(1500.0)
        assert resultado["desconto_irrf"] == 0.0

    def test_salario_invalido_zero(self):
        with pytest.raises(ValueError):
            calcular_salario_estagiario(0.0)

    def test_salario_invalido_negativo(self):
        with pytest.raises(ValueError):
            calcular_salario_estagiario(-500.0)


class TestCLT:

    def test_desconto_inss_aplicado(self):
        resultado = calcular_salario_clt(3000.0)
        assert resultado["desconto_inss"] == pytest.approx(240.0)

    def test_desconto_irrf_acima_do_limite(self):
        resultado = calcular_salario_clt(3000.0)
        assert resultado["desconto_irrf"] == pytest.approx(300.0)

    def test_salario_liquido_com_todos_descontos(self):
        resultado = calcular_salario_clt(3000.0)
        assert resultado["salario_liquido"] == pytest.approx(2460.0)

    def test_sem_irrf_abaixo_do_limite(self):
        # Salário exatamente em R$ 2000 não gera IRRF
        resultado = calcular_salario_clt(2000.0)
        assert resultado["desconto_irrf"] == 0.0

    def test_sem_irrf_abaixo_de_2000(self):
        resultado = calcular_salario_clt(1800.0)
        assert resultado["desconto_irrf"] == 0.0
        assert resultado["desconto_inss"] == pytest.approx(144.0)

    def test_salario_invalido(self):
        with pytest.raises(ValueError):
            calcular_salario_clt(-1.0)

class TestFreelancer:

    def test_salario_bruto_correto(self):
        resultado = calcular_salario_freelancer(40, 50.0)
        assert resultado["salario_bruto"] == pytest.approx(2000.0)

    def test_desconto_cinco_por_cento(self):
        resultado = calcular_salario_freelancer(40, 50.0)
        assert resultado["desconto_inss"] == pytest.approx(100.0)

    def test_salario_liquido(self):
        resultado = calcular_salario_freelancer(40, 50.0)
        assert resultado["salario_liquido"] == pytest.approx(1900.0)

    def test_sem_irrf(self):
        resultado = calcular_salario_freelancer(40, 50.0)
        assert resultado["desconto_irrf"] == 0.0

    def test_horas_invalidas(self):
        with pytest.raises(ValueError):
            calcular_salario_freelancer(0, 50.0)

    def test_valor_hora_invalido(self):
        with pytest.raises(ValueError):
            calcular_salario_freelancer(40, 0.0)
