import logging
import os
from typing import List

logger = logging.getLogger(__name__)

# Rótulos amigáveis para cada tipo de funcionário
ROTULOS_TIPO: dict = {
    "estagiario": "Estagiário",
    "clt": "CLT",
    "freelancer": "Freelancer",
}

SEPARADOR: str = "-" * 30


def _formatar_registro(registro: dict) -> str:
   
    tipo_label = ROTULOS_TIPO.get(registro["tipo"], registro["tipo"].capitalize())

    linhas = [
        f"Nome: {registro['nome']}",
        f"Tipo: {tipo_label}",
        f"Salário Bruto: R$ {registro['salario_bruto']:.2f}",
        f"Desconto INSS: R$ {registro['desconto_inss']:.2f}",
        f"Desconto IRRF: R$ {registro['desconto_irrf']:.2f}",
        f"Salário Líquido: R$ {registro['salario_liquido']:.2f}",
        SEPARADOR,
    ]
    return "\n".join(linhas)


def gerar_relatorio(registros: List[dict]) -> str:
    
    if not registros:
        return "Nenhum funcionário cadastrado."

    total_pago = sum(r["salario_liquido"] for r in registros)

    secoes = ["=== Relatório de Folha de Pagamento ===\n"]
    for registro in registros:
        secoes.append(_formatar_registro(registro))

    secoes.append(f"\nTotal pago pela empresa: R$ {total_pago:.2f}")
    return "\n".join(secoes)


def exibir_relatorio(registros: List[dict]) -> None:
   
    print("\n" + gerar_relatorio(registros))
    logger.info("Relatório exibido para %d funcionário(s).", len(registros))


def salvar_relatorio(registros: List[dict], caminho: str) -> bool:
    
    conteudo = gerar_relatorio(registros)

    try:
        diretorio = os.path.dirname(caminho)
        if diretorio:
            os.makedirs(diretorio, exist_ok=True)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)

        print(f" Relatório salvo em: {caminho}")
        logger.info("Relatório salvo em: %s", caminho)
        return True

    except (OSError, ValueError) as erro:
        print(f" Não foi possível salvar o relatório: {erro}")
        logger.error("Falha ao salvar relatório em %s: %s", caminho, erro)
        return False
