import sphinx_rtd_theme

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Semillero Sophia'
copyright = '2026, CarlosMahecha'
author = 'CarlosMahecha'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_baseurl = ""
html_favicon = "_static/logoSophia.png"
html_title = "Documentación"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 2,
}
# Sirve para ubicar la carpeta que contiene el CSS
html_static_path = ['_static']  
# Carga el archivo que contiene el diseño (CSS)
html_css_files = [
    'custom.css',
]

html_js_files = []          # evita conflictos de rutas JS
html_extra_path = []        # evita rutas raras