# meu_projeto – Calculadora Python

Projeto desenvolvido como **Atividade Prática** do curso do Prof. Maxwell Gomes,
aplicando todas as boas práticas de desenvolvimento Python aprendidas na Aula 1.

---

## Funcionalidades

- **Multiplicar**, **Somar**, **Subtrair** e **Dividir** dois números
- Validação de entrada (ex.: divisão por zero lança `ValueError`)
- Registro de eventos via `logging` em `app.log`
- Testes automatizados com `pytest`
- Documentação gerada com `Sphinx`

---

## Estrutura do Projeto

```
meu_projeto/
├── src/
│   └── meu_projeto/
│       ├── __init__.py
│       ├── main.py                  # Programa principal
│       └── utils/
│           ├── __init__.py
│           └── calculadora.py       # Operações matemáticas
├── tests/
│   └── test_calculadora.py          # Testes com pytest
├── docs/                            # Documentação Sphinx
├── requirements.txt
└── README.md
```

---

## Instalação

### 1. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac / Linux
source .venv/bin/activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Como Usar

Execute o programa principal:

```bash
python src/meu_projeto/main.py
```

Saída esperada:

```
4 x 5 = 20
10 + 7 = 17
15 - 6 = 9
20 / 4 = 5.0
```

Os eventos também são gravados em `app.log`.

---

## Executando os Testes

```bash
pytest tests/
```

---

## Verificações de Qualidade

```bash
# Formatação automática (PEP 8)
black src/ tests/

# Verificação de estilo
flake8 src/

# Verificação de tipos
mypy src/
```

---

## Gerando a Documentação (Sphinx)

```bash
cd docs
sphinx-quickstart   # apenas na primeira vez
make html           # gera a documentação em docs/_build/html/
```

Abra `docs/_build/html/index.html` no navegador para ver o resultado.

---

## Boas Práticas Aplicadas (Aula 1)

| Prática | Onde |
|---|---|
| Estrutura `src/` com pacotes | `src/meu_projeto/` e `utils/` |
| Docstrings estilo Google | Todas as funções |
| Type hints | Todos os parâmetros e retornos |
| Constantes nomeadas | — (sem constantes mágicas) |
| Nomeação snake_case / PEP 8 | Todo o projeto |
| Logging com `basicConfig` | `main.py` |
| Tratamento de erros | `dividir()` — `ValueError` |
| Testes com `pytest` | `tests/test_calculadora.py` |
| `if __name__ == "__main__"` | Não necessário (módulo simples) |
| README completo | Este arquivo |

---

## Contato

Prof. Maxwell Gomes – [LinkedIn](https://www.linkedin.com/in/mxyconsulting)
