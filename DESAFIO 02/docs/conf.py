"""Configuração do Sphinx para geração de documentação do meu_projeto."""

import os
import sys

# Permite que o Sphinx encontre o pacote para autodoc
sys.path.insert(0, os.path.abspath("../src"))

# ── Informações do projeto ────────────────────────────────────────────────────
project = "meu_projeto"
copyright = "2024, Prof. Maxwell Gomes"
author = "Prof. Maxwell Gomes"
release = "1.0.0"

# ── Extensões ─────────────────────────────────────────────────────────────────
extensions = [
    "sphinx.ext.autodoc",       # Gera docs a partir de docstrings
    "sphinx.ext.napoleon",      # Suporte ao estilo Google de docstring
    "sphinx.ext.viewcode",      # Adiciona links para o código-fonte
]

# ── Template e tema ───────────────────────────────────────────────────────────
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
