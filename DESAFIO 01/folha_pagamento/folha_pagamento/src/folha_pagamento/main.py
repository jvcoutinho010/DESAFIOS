import logging
import os
import sys
from typing import List
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
 
from folha_pagamento.utils.cadastro import cadastrar_funcionario, processar_salario
from folha_pagamento.utils.relatorio import exibir_relatorio, salvar_relatorio
 
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)
 
def menu_cadastrar(registros: List[dict]) -> None:
    
    dados = cadastrar_funcionario()
    if dados is None:
        print("  Cadastro cancelado.")
        return
 
    registro = processar_salario(dados)
    if registro is None:
        print(" Não foi possível processar o funcionário. Verifique os dados.")
        return
 
    registros.append(registro)
    print(f" {registro['nome']} cadastrado com sucesso!")
 
 
def menu_gerar_relatorio(registros: List[dict]) -> None:
    
    if not registros:
        print("\n  Nenhum funcionário cadastrado ainda.")
        return
    exibir_relatorio(registros)
 
 
def menu_salvar_relatorio(registros: List[dict]) -> None:
    
    if not registros:
        print("\n  Nenhum funcionário cadastrado para salvar.")
        return
 
    caminho_padrao = os.path.join(os.getcwd(), "relatorio_folha.txt")
    caminho = (
        input(f"\nCaminho do arquivo [{caminho_padrao}]: ").strip()
        or caminho_padrao
    )
    salvar_relatorio(registros, caminho)
 
 
def exibir_menu() -> None:
    """Exibe as opções do menu principal no console."""
    print("\n" + "=" * 40)
    print("   Sistema de Folha de Pagamento")
    print("=" * 40)
    print("  1. Cadastrar funcionário")
    print("  2. Gerar relatório")
    print("  3. Salvar relatório em arquivo")
    print("  4. Sair")
    print("=" * 40)
 
def main() -> None:
   
    logger.info("Sistema de folha de pagamento iniciado.")
    registros: List[dict] = []
 
    opcoes = {
        "1": lambda: menu_cadastrar(registros),
        "2": lambda: menu_gerar_relatorio(registros),
        "3": lambda: menu_salvar_relatorio(registros),
    }
 
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
 
        if escolha == "4":
            print("\n  Até logo!")
            logger.info("Sistema encerrado pelo usuário.")
            break
 
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("  ✗ Opção inválida. Escolha entre 1 e 4.")
 
 
if __name__ == "__main__":
    main()