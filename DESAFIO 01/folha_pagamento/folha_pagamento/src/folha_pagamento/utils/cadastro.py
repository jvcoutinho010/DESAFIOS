"""Módulo responsável pelo cadastro e processamento de funcionários.

Gerencia a entrada de dados, validação e a montagem dos registros
de cada funcionário no sistema.
"""

import logging
from typing import Optional

from folha_pagamento.utils.calculos import (
    calcular_salario_clt,
    calcular_salario_estagiario,
    calcular_salario_freelancer,
)

# Tipos de funcionários aceitos pelo sistema
TIPOS_VALIDOS: tuple = ("estagiario", "clt", "freelancer")

logger = logging.getLogger(__name__)


def _solicitar_float(mensagem: str) -> Optional[float]:
    """Solicita ao usuário um número de ponto flutuante.

    Args:
        mensagem (str): Texto exibido ao usuário.

    Returns:
        Optional[float]: Valor inserido ou None em caso de entrada inválida.
    """
    try:
        valor = float(input(mensagem).strip().replace(",", "."))
        return valor
    except ValueError:
        print("  ✗ Entrada inválida. Digite um número (ex.: 3000 ou 3000.50).")
        return None


def cadastrar_funcionario() -> Optional[dict]:
    """Coleta e valida os dados de um novo funcionário.

    Solicita nome, tipo e informações salariais específicas de acordo
    com o tipo escolhido. Retorna None se o usuário cancelar ou fornecer
    dados inválidos repetidamente.

    Returns:
        Optional[dict]: Dicionário com os dados brutos do funcionário
                        ou None se o cadastro for cancelado.
    """
    print("\n--- Cadastro de Funcionário ---")

    # Validação do nome
    nome = input("Nome do funcionário (ou 'cancelar'): ").strip()
    if nome.lower() == "cancelar":
        return None
    if not nome:
        print("  ✗ O nome não pode ser vazio.")
        return None

    # Validação do tipo
    tipo = input("Tipo (estagiario / clt / freelancer): ").strip().lower()
    if tipo not in TIPOS_VALIDOS:
        print(f"  ✗ Tipo inválido. Escolha entre: {', '.join(TIPOS_VALIDOS)}.")
        return None

    # Coleta de informações salariais conforme o tipo
    if tipo == "estagiario":
        salario = _solicitar_float("Salário fixo mensal (R$): ")
        if salario is None:
            return None
        dados = {"nome": nome, "tipo": tipo, "salario": salario}

    elif tipo == "clt":
        salario = _solicitar_float("Salário bruto mensal (R$): ")
        if salario is None:
            return None
        dados = {"nome": nome, "tipo": tipo, "salario": salario}

    else:  # freelancer
        horas = _solicitar_float("Horas trabalhadas no mês: ")
        if horas is None:
            return None
        valor_hora = _solicitar_float("Valor por hora (R$): ")
        if valor_hora is None:
            return None
        dados = {
            "nome": nome,
            "tipo": tipo,
            "horas": horas,
            "valor_hora": valor_hora,
        }

    logger.info("Funcionário cadastrado: %s (%s)", nome, tipo)
    return dados


def processar_salario(dados: dict) -> Optional[dict]:
    
    tipo = dados["tipo"]
    nome = dados["nome"]

    try:
        if tipo == "estagiario":
            resultado = calcular_salario_estagiario(dados["salario"])
        elif tipo == "clt":
            resultado = calcular_salario_clt(dados["salario"])
        else:  # freelancer
            resultado = calcular_salario_freelancer(
                dados["horas"], dados["valor_hora"]
            )
    except ValueError as erro:
        print(f"Erro ao calcular salário de {nome}: {erro}")
        logger.warning("Erro ao processar funcionário %s: %s", nome, erro)
        return None

    registro = {"nome": nome, "tipo": tipo, **resultado}
    logger.info(
        "Salário processado – %s | Líquido: R$ %.2f",
        nome,
        resultado["salario_liquido"],
    )
    return registro
