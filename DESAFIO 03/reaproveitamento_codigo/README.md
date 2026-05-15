# Reaproveitamento de Código

Um projeto para aprender reutilização de código em Python.

## Funcionalidades

- Funções matemáticas reutilizáveis: `cubo`, `quadrado`, `raiz_quadrada`
- Decorador `medir_tempo` que registra automaticamente o tempo de execução
- Logging de eventos em `app.log`
- Testes automatizados com `pytest`
- Documentação gerada com Sphinx

## Estrutura do Projeto

```
reaproveitamento_codigo/
├── src/
│   ├── main.py              # Programa principal
│   └── utils/
│       ├── __init__.py
│       └── math_utils.py    # Funções matemáticas + decorador medir_tempo
├── tests/
│   └── test_math_utils.py   # Testes automatizados
├── docs/
│   ├── conf.py              # Configuração do Sphinx
│   └── index.rst
├── requirements.txt
└── README.md
```

## Como Usar

1. Crie um ambiente virtual: `python -m venv .venv`
2. Ative: `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Mac/Linux)
3. Instale dependências: `pip install pytest`
4. Execute: `python src/main.py`

## Executando os Testes

```bash
pytest tests/
```

## Verificações de Qualidade

```bash
pip install flake8 mypy
flake8 src/
mypy src/
```

## Gerando a Documentação (Sphinx)

```bash
pip install sphinx sphinx-rtd-theme
cd docs
sphinx-quickstart   # apenas na primeira vez
make html
```

## Contato

Pergunte ao Prof. Maxwell Gomes!
