import logging
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402

from meu_projeto.utils.calculadora import (  # noqa: E402
    dividir, multiplicar, somar, subtrair
)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

logger.info("Iniciando cálculo")

resultado = multiplicar(4, 5)
logger.info(f"Resultado multiplicar(4, 5): {resultado}")
print(f"4 x 5 = {resultado}")

resultado = somar(10, 7)
logger.info(f"Resultado somar(10, 7): {resultado}")
print(f"10 + 7 = {resultado}")

resultado = subtrair(15, 6)
logger.info(f"Resultado subtrair(15, 6): {resultado}")
print(f"15 - 6 = {resultado}")

resultado = dividir(20, 4)
logger.info(f"Resultado dividir(20, 4): {resultado}")
print(f"20 / 4 = {resultado}")

logger.info("Cálculos finalizados com sucesso")
