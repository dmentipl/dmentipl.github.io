# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'dmentipl'
copyright = '2021, Daniel Mentiplay'
author = 'Daniel Mentiplay'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    "README.md",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "search_bar_text": "Search...",
    "external_links": [
        {"name": "Cocktails", "url": "https://dmentipl.github.io/cocktails/"},
        {"name": "Recipes", "url": "https://dmentipl.github.io/recipes/"},
    ],
    "footer_items": ["copyright", "last-updated"],
    "navbar_end": ["search-field"],
    "show_prev_next": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["template.html"],
    "posts": ['tagcloud.html', 'archives.html'],
    "posts/**": ['postcard.html', 'recentposts.html', 'archives.html'],
}
html_last_updated_fmt = '%b %d, %Y'

# Blog
blog_baseurl = "https://dmentipl.github.io"
blog_title = "Daniel Mentiplay"
blog_path = "posts"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_admonition_enable = True
myst_deflist_enable = True


def setup(app):
    app.add_css_file("custom.css")
