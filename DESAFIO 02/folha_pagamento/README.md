# Sistema de Folha de Pagamento

Projeto desenvolvido como desafio da **Aula 2** do curso do Prof. Maxwell Gomes,
aplicando as boas práticas de desenvolvimento Python ensinadas na **Aula 1**.

## Funcionalidades

- Cadastro de funcionários: **Estagiário**, **CLT** e **Freelancer**
- Cálculo automático de INSS e IRRF conforme as regras de cada tipo
- Geração de relatório detalhado no console
- Salvamento do relatório em arquivo de texto
- Tratamento de erros de entrada e de escrita em arquivo
- Logging de eventos em `app.log`

## Estrutura do Projeto

```
folha_pagamento/
├── src/
│   └── folha_pagamento/
│       ├── __init__.py
│       ├── main.py              # Ponto de entrada / menu interativo
│       └── utils/
│           ├── __init__.py
│           ├── calculos.py      # Regras de cálculo de salário
│           ├── cadastro.py      # Cadastro e validação de funcionários
│           └── relatorio.py     # Geração e salvamento do relatório
├── tests/
│   ├── test_calculos.py
│   └── test_relatorio.py
├── docs/
├── requirements.txt
└── README.md
```

## Instalação

1. Clone ou copie o projeto para sua máquina.
2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Usar

Execute o programa principal a partir da pasta raiz do projeto:

```bash
python src/folha_pagamento/main.py
```

Siga o menu interativo:
- **1** – Cadastrar funcionário
- **2** – Gerar relatório no console
- **3** – Salvar relatório em arquivo `.txt`
- **4** – Sair

## Executando os Testes

```bash
pytest tests/
```

## Verificações de Qualidade

```bash
# Formatação automática
black src/ tests/

# Verificação de estilo PEP 8
flake8 src/ tests/

# Verificação de tipos
mypy src/
```

## Regras de Negócio

| Tipo        | Cálculo do Bruto          | INSS | IRRF (se bruto > R$ 2000) |
|-------------|---------------------------|------|---------------------------|
| Estagiário  | Salário fixo mensal       | 0%   | 0%                        |
| CLT         | Salário bruto mensal      | 8%   | 10%                       |
| Freelancer  | Horas × Valor/hora        | 5%\* | 0%                        |

\* Para freelancers, o desconto único de 5% é exibido na coluna INSS.

## Contato

Prof. Maxwell Gomes – [LinkedIn](https://www.linkedin.com/in/mxyconsulting)
