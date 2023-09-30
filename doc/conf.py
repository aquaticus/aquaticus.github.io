project = 'Aquaticus Docs'
copyright = '2023, Aquaticus'
author = 'aquaticus'
extensions = ['sphinx_copybutton', 'sphinx.ext.intersphinx', 'sphinxext.opengraph', 'sphinxcontrib.youtube']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
source_suffix = {'.rst': 'restructuredtext'}
html_show_sphinx=False
html_show_sourcelink = False
intersphinx_mapping = {
    "esphome": ("https://esphome.io/", None),
}
intersphinx_disabled_reftypes = ["*"]
