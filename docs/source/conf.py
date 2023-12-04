# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SNP/GWAS workflow'
copyright = '2023, MIT'
author = 'Martin, Tatiana, Yiden'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.mathjax',
  'sphinxcontrib.mermaid',
  'sphinxext.rediraffe',
  'sphinx_rtd_theme',
  'myst_parser'
]

myst_enable_extensions = ['colon_fence', 'deflist', 'dollarmath']
myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = []

# The suffix of source filenames.
source_suffix = '.md'

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
  'logo_only': True,
  'display_version': False
}

html_context = {
    "display_github": True,
    "conf_py_path": "/docs/"
}

html_static_path = ['_static']
extensions = ["myst_parser"]

html_css_files = [
    'css/custom.css',
]

html_sidebars = {
    '**': ['globaltoc.html']
}






