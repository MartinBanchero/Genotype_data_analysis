# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Genotype data analysis UMCG-GRIAC'
copyright = '2023, Martin Banchero, Tatiana Karp'
author = 'Martin, Tatiana'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []
extensions = [
  'sphinx.ext.mathjax',
  'sphinxcontrib.mermaid',
  'sphinxext.rediraffe',
  'sphinx_rtd_theme',
  'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
#html_theme = 'furo'
#html_theme = 'alabaster'
html_static_path = ['_static']

extensions = ["myst_parser"]
html_css_files = [
    'css/custom.css',
]

