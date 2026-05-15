import logging
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from utils.math_utils import cubo, medir_tempo  # noqa: E402

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    encoding="utf-8",
)


@medir_tempo
def calcular_cubo(n: float) -> float:
    
    logging.info(f"Calculando cubo de {n}")
    return cubo(n)

resultado = calcular_cubo(3)
logging.info(f"Resultado: {resultado}")
print(f"Cubo de 3: {resultado}")

resultado2 = calcular_cubo(5)
logging.info(f"Resultado: {resultado2}")
print(f"Cubo de 5: {resultado2}")

resultado3 = calcular_cubo(-2)
logging.info(f"Resultado: {resultado3}")
print(f"Cubo de -2: {resultado3}")
