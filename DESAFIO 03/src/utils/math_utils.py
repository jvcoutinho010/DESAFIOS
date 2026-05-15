import functools
import logging
import time
from typing import Callable, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable)

def medir_tempo(func: F) -> F:
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        duracao = time.perf_counter() - inicio
        logger.info(
            "Função '%s' executada em %.6f segundos.", func.__name__, duracao
        )
        return resultado

    return wrapper  # type: ignore[return-value]


def cubo(numero: float) -> float:
    
    return numero ** 3


def quadrado(numero: float) -> float:
    
    return numero ** 2


def raiz_quadrada(numero: float) -> float:
    
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de número negativo.")
    return numero ** 0.5
