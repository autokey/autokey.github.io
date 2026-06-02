# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, as shown here.
#
import os
import sys
import re

# -- Source information ------------------------------------------------------

# Determine the absolute path to this conf.py file:
base_path = os.path.dirname(os.path.abspath(__file__))

# Define the two possible (local or remote) paths to the AutoKey source code:
# 1. Local/Tox path: autokey is a sibling to the docs folder:
local_path = os.path.join(base_path, "..", "autokey")
# 2. GitHub Actions path: autokey is inside the docs folder:
github_path = os.path.join(base_path, "autokey")

# Select the correct path based on which one actually exists and print a breadcrumb to the log:
if os.path.exists(local_path):
    # This is what you'll see in your local tox tests:
    print("Sphinx Config: Using local/tox path structure 🚀")
    autokey_root = local_path
else:
    # This is what you'll see in the GitHub Action logs:
    print("Sphinx Config: Using GitHub Actions path structure 🚀")
    autokey_root = github_path

# Point Sphinx to the library so it can generate API docs:
sys.path.insert(0, os.path.join(autokey_root, "lib"))

# Use logic from the autokey/setup.py file to get the AutoKey version:
def get_autokey_version():
    source_file_name = os.path.join(autokey_root, "lib", "autokey", "common.py")
    
    try:
        with open(source_file_name, "r") as metadata_source_file:
            source = metadata_source_file.read()
    except FileNotFoundError:
        print(f"Critical Error: Cannot find AutoKey source at {source_file_name}")
        sys.exit(1)

    def search_for(pattern: str) -> str:
        match = re.search(
            r"""^{}\s*=\s*('(.*)'|"(.*)")""".format(pattern),
            source,
            re.M
        )
        # match.group(1) captures the outer quotes along with the text.
        # [1:-1] removes the outer quotes to yield just the version.
        # The full version, including alpha/beta/rc tags, is returned:
        return match.group(1)[1:-1] if match else "unknown"

    return search_for("VERSION")

# -- Project information -----------------------------------------------------

project = 'AutoKey'
# Is there some way to have this be a link to github authors page?
author = 'various'
copyright = '2023, various'
release = version = get_autokey_version()

# -- General configuration ---------------------------------------------------

# List of Sphinx extension module names grouped by purpose since they're
# processed in the listed order. Both native (named 'sphinx.ext.*') and
# custom extensions are accepted:
extensions = [
    # Core Sphinx extensions:
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    # Format parsers and styling:
    'recommonmark',
    'sphinx_rtd_theme',
    # Third-party code documenters:
    'enum_tools.autoenum',
    'sphinx_epytext',
]

# Map file extensions to their respective markup languages:
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# List of paths, relative to the documentation root directory, that contain
# templates:
templates_path = [
    '_templates',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'autokey/**',      # Prevents Sphinx from tracking cloned code files as stand-alone pages
    '**/.DS_Store',    # Prevents Sphinx from tracking the macOS hidden **Desktop Services Store** file
    '**/__MACOSX/**',  # Prevents Sphinx from tracking macOS zip metadata directories
    '**/._*',          # Prevents Sphinx from tracking macOS AppleDouble metadata files
    'guides/**',       # Prevents Sphinx from tracking all guides including future potential sub-directories
    '*.md',            # Prevents Sphinx from tracking all Markdown in the root directory
    '**/Thumbs.db',    # Prevents Sphinx from tracking all nested Windows thumbnail caches
   '**/.venv/**',      # Prevents Sphinx from tracking all nested virtual environments
]

# -- HTML configuration ------------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the Sphinx documentation
# for a list of built-in themes:
html_theme = 'sphinx_rtd_theme'

# List of paths, relative to the documentation root directory, to custom
# static files (such as style-sheets). These files are copied over after the
# built-in static files, overwriting them:
html_static_path = [
    '_static',
]

# Only apply custom CSS style to PDF builds:
if 'simplepdf' in sys.argv:
    html_css_files = ['custom.css']
else:
    html_css_files = []

# Only suppress creation of "Indices and Tables" for PDF builds:
if 'simplepdf' in sys.argv:
    html_use_index = False
else:
    html_use_index = True

html_logo = 'autokey.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

html_favicon = 'favicon.ico'

# Location of the hosted source files passed to templates. Enables the
# "Edit on GitHub" behavior in the top right corners of HTML pages:
html_context = {
    'display_github': True,
    'github_user': 'autokey',
    'github_repo': 'autokey.github.io',
    'github_version': 'master/',
}

# List of modules used by the sphinx.ext.autodoc extension to tell Sphinx to
# fake (mock) specific Python modules during the documentation build process.
autodoc_mock_imports = [
    "gi",
    "pyatspi",
    "PyQt5",
    "tkinter",
    "Tkinter"
]

# Work-around for the module docstring being posted at the top of every API
# page:
def skip_modules_docstring(app, what, name, obj, options, lines):
    print(what, name)
    if what == 'module':
        print(what, name, lines)
        del lines[:]

# Register a Sphinx hook to modify or skip specific docstrings during the build process:
def setup(app):
    app.connect('autodoc-process-docstring', skip_modules_docstring)

# -- PDF configuration -------------------------------------------------------

# Use AutoKey release version in PDF file names:
simplepdf_file_name = f"AutoKey_v{release}.pdf"
# Control style of the PDF and its single-file HTML artifact:
simplepdf_vars = {
    'cover': '#ffffff',     # use for cover text
    'cover-bg': '#598bb9',  # use for cover page
    'primary': '#598bb9',   # use for accents
}
