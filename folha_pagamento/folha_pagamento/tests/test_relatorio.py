import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from folha_pagamento.utils.relatorio import gerar_relatorio, salvar_relatorio

REGISTRO_CLT = {
    "nome": "João Silva",
    "tipo": "clt",
    "salario_bruto": 3000.0,
    "desconto_inss": 240.0,
    "desconto_irrf": 300.0,
    "salario_liquido": 2460.0,
}

REGISTRO_ESTAGIARIO = {
    "nome": "Maria Souza",
    "tipo": "estagiario",
    "salario_bruto": 1500.0,
    "desconto_inss": 0.0,
    "desconto_irrf": 0.0,
    "salario_liquido": 1500.0,
}


class TestGerarRelatorio:

    def test_sem_funcionarios(self):
        resultado = gerar_relatorio([])
        assert "Nenhum funcionário" in resultado

    def test_contem_nome_funcionario(self):
        resultado = gerar_relatorio([REGISTRO_CLT])
        assert "João Silva" in resultado

    def test_contem_total_pago(self):
        resultado = gerar_relatorio([REGISTRO_CLT, REGISTRO_ESTAGIARIO])
        assert "3960.00" in resultado  # 2460 + 1500

    def test_tipo_formatado_corretamente(self):
        resultado = gerar_relatorio([REGISTRO_CLT])
        assert "CLT" in resultado


class TestSalvarRelatorio:

    def test_arquivo_criado(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            caminho = os.path.join(tmpdir, "teste.txt")
            sucesso = salvar_relatorio([REGISTRO_CLT], caminho)
            assert sucesso is True
            assert os.path.exists(caminho)

    def test_conteudo_do_arquivo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            caminho = os.path.join(tmpdir, "teste.txt")
            salvar_relatorio([REGISTRO_CLT], caminho)
            with open(caminho, encoding="utf-8") as f:
                conteudo = f.read()
            assert "João Silva" in conteudo

    def test_caminho_invalido_retorna_false(self):
        # Usa um nome de arquivo com caractere nulo, que é sempre inválido no SO
        sucesso = salvar_relatorio([REGISTRO_CLT], "/tmp/arquivo\x00invalido.txt")
        assert sucesso is False
