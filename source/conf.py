# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime
sys.path.insert(0, os.path.abspath("../src"))

copyright = f"2025-{datetime.now().year}, mroczect.org"
project = "from-zero-to-dev"
author = "mroczect.org"
version = "0.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgconverter",
    # Markdown support
    "myst_parser",
    # API documentation
    "sphinxcontrib.autodoc_pydantic",
    # Content tabs
    "sphinx_inline_tabs",
    # Design improvements
    "sphinx_design",
    # Copy button for code blocks
    "sphinx_copybutton",
    # Diagrams and charts
    "sphinxcontrib.mermaid",
    # Search improvements
    "sphinx_search.extension",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", "requirements.txt"]

# Default language
language = "en"

# Enable figure numbering
numfig = True
numfig_format = {
    "figure": "Figure %s",
    "table": "Table %s",
    "code-block": "Listing %s",
}

nitpicky = True

# -- Internationalization configuration --------------------------------------
locale_dirs = ["locale/"]  # path for translations
gettext_compact = False
gettext_uuid = True

# -- Extension configuration -------------------------------------------------

# Autodoc configuration
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
autodoc_mock_imports = ["optional_dependency"]
autoclass_content = "both"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = {"CustomType": "mypackage.CustomClass"}

# Autosummary configuration
autosummary_generate = True
autosummary_generate_overwrite = True
autosummary_imported_members = False

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
}

# Graphviz configuration
graphviz_output_format = "svg"
graphviz_dot_args = [
    "-Gfontname=Helvetica",
    "-Nfontname=Helvetica",
    "-Efontname=Helvetica",
]

# MyST Parser configuration
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 6
myst_substitutions = {"version": version, "project": project}

# Todo configuration
todo_include_todos = True
todo_link_only = False
todo_emit_warnings = False

# Copybutton configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

html_theme = "sphinxdoc"

html_title = f"{project} {version} Documentation"
html_static_path = ["_static"]
html_css_files = ["./_static/web/css/custom.css"]
html_js_files = ["./_static/web/js/custom.js"]
html_logo = "./_static/image/icon/fz-dev.png"
html_favicon = "./_static/image/icon/fz-dev.ico"
html_show_sourcelink = True
html_copy_source = True
html_sourcelink_suffix = ".txt"
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

latex_engine = "xelatex"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "preamble": r"""
        \usepackage[UTF8]{ctex}
        \setcounter{tocdepth}{3}
    """,
}
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ["search.html"]
def setup(app):
    app.add_css_file("./_static/web/css/custom.css")
    app.add_js_file("./_static/web/js/custom.js")
    app.connect("builder-inited", lambda app: print("Build started!"))
    app.connect("build-finished", lambda app, exception: print("Build finished!"))
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".txt": "restructuredtext",
}
master_doc = "index"
