PERCENTUAL_INSS_CLT: float = 0.08
PERCENTUAL_IRRF_CLT: float = 0.10
SALARIO_BASE_IRRF: float = 2000.00
PERCENTUAL_DESCONTO_FREELANCER: float = 0.05


def calcular_salario_estagiario(salario_fixo: float) -> dict:
   
    if salario_fixo <= 0:
        raise ValueError("O salário deve ser maior que zero.")

    return {
        "salario_bruto": salario_fixo,
        "desconto_inss": 0.0,
        "desconto_irrf": 0.0,
        "salario_liquido": salario_fixo,
    }


def calcular_salario_clt(salario_bruto: float) -> dict:
    
    if salario_bruto <= 0:
        raise ValueError("O salário deve ser maior que zero.")

    desconto_inss = salario_bruto * PERCENTUAL_INSS_CLT

    desconto_irrf = (
        salario_bruto * PERCENTUAL_IRRF_CLT
        if salario_bruto > SALARIO_BASE_IRRF
        else 0.0
    )

    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_inss,
        "desconto_irrf": desconto_irrf,
        "salario_liquido": salario_liquido,
    }


def calcular_salario_freelancer(horas_trabalhadas: float, valor_hora: float) -> dict:
    
    if horas_trabalhadas <= 0:
        raise ValueError("As horas trabalhadas devem ser maiores que zero.")
    if valor_hora <= 0:
        raise ValueError("O valor por hora deve ser maior que zero.")

    salario_bruto = horas_trabalhadas * valor_hora
    desconto = salario_bruto * PERCENTUAL_DESCONTO_FREELANCER
    salario_liquido = salario_bruto - desconto

    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto,
        "desconto_irrf": 0.0,
        "salario_liquido": salario_liquido,
    }
