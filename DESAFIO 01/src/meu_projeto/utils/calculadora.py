"""Módulo de operações matemáticas básicas.

Fornece funções puras para as quatro operações fundamentais,
com validação de entrada e documentação completa.
"""


def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números.

    Args:
        a (float): Primeiro fator.
        b (float): Segundo fator.

    Returns:
        float: O produto de a e b.

    Examples:
        >>> multiplicar(4, 5)
        20
        >>> multiplicar(2.5, 4)
        10.0
    """
    return a * b


def somar(a: float, b: float) -> float:
    """Soma dois números.

    Args:
        a (float): Primeira parcela.
        b (float): Segunda parcela.

    Returns:
        float: A soma de a e b.

    Examples:
        >>> somar(3, 7)
        10
    """
    return a + b


def subtrair(a: float, b: float) -> float:
    """Subtrai b de a.

    Args:
        a (float): Minuendo.
        b (float): Subtraendo.

    Returns:
        float: A diferença entre a e b.

    Examples:
        >>> subtrair(10, 3)
        7
    """
    return a - b


def dividir(a: float, b: float) -> float:
    """Divide a por b.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: O quociente da divisão de a por b.

    Raises:
        ValueError: Se b for zero.

    Examples:
        >>> dividir(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
