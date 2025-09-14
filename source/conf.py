# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# Jika perlu mengimpor modul proyek (untuk autodoc)
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

copyright = f"2025-{datetime.now().year}, mroczect.org"
project = "from-zero-to-dev"
author = "mroczect.org"
version = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Daftar ekstensi yang digunakan
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

# Template paths
templates_path = ["_templates"]

# Exclude patterns
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

# Strict reference checking
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

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinxdoc"

# Konfigurasi tema Furo
html_theme_options = {
    "announcement": "🚧 This documentation is under construction!",
    "source_repository": "https://github.com/yourusername/yourrepository/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourusername/yourrepository",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "navigation_with_keys": True,
}

# Opsi untuk PyData theme
# html_theme_options = {
#     "github_url": "https://github.com/yourusername/yourrepository",
#     "twitter_url": "https://twitter.com/yourusername",
#     "show_toc_level": 2,
#     "navbar_align": "left",
# }

html_title = f"{project} {version} Documentation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
html_show_sourcelink = True
html_copy_source = True
html_sourcelink_suffix = ".txt"
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# -- Options for PDF output --------------------------------------------------
latex_engine = "xelatex"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "preamble": r"""
        \usepackage[UTF8]{ctex}
        \setcounter{tocdepth}{3}
    """,
}

# -- Options for EPUB output -------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ["search.html"]


# -- Custom setup ------------------------------------------------------------
def setup(app):
    app.add_css_file("custom.css")
    app.add_js_file("custom.js")
    app.connect("builder-inited", lambda app: print("Build started!"))
    app.connect("build-finished", lambda app, exception: print("Build finished!"))


# -- Source suffixes ---------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".txt": "restructuredtext",
}

# -- Master document ---------------------------------------------------------
master_doc = "index"
