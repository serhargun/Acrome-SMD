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
sys.path.insert(0, os.path.abspath('./exts')) 

project = 'Acrome Smart Motor Drivers'
copyright = '2023, Acrome Robotics'
author = 'Acrome Robotics'

# -- General configuration

extensions = [
    'sphinx_rtd_theme', # read the docs theme
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc', # Generate documentation from Python modules
    'sphinx.ext.autosummary', # Generate summary tables for Python documentation
    'sphinx.ext.intersphinx',  # Hyperlinks to external projects (such as Python standard library)
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_id':'XXX',
    'style_external_links': False,
    'display_version': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

release = '0.1'
version = '0.1.0'
