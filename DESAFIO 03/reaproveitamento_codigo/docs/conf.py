"""Configuração do Sphinx para o projeto reaproveitamento_codigo."""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "reaproveitamento_codigo"
copyright = "2024, Prof. Maxwell Gomes"
author = "Prof. Maxwell Gomes"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
