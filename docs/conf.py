# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./figures'))
sys.path.insert(0, os.path.abspath('./exts')) # needed for fibre_autodoc extension
sys.path.insert(0, os.path.abspath('../tools/fibre-tools')) # needed for fibre_autodoc extension

project = 'Acrome Actuator Board'
copyright = '2022, Acrome Robotics'
author = 'Acrome Robotics'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx_rtd_theme', # read the docs theme
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc', # Generate documentation from Python modules
    'sphinx.ext.autosummary', # Generate summary tables for Python documentation
    'sphinx.ext.intersphinx',  # Hyperlinks to external projects (such as Python standard library)
    'fibre_autodoc', # Generate summary tables for Python documentation
    'myst_parser' # render CHANGELOG markdown file
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_id':'XXX',
    'style_external_links': True,
    'display_version': True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

release = '0.1'
version = '0.1.0'
