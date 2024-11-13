# Autokey Documentation

Built using [sphinx]().

Uses the [sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) extension to automatically generate API documentation. This module imports the modules and reads the documentation for each function and generates the API documentation based on that.

Uses the [sphinx epytext]() extension to convert older style epydoc documentation format to sphinx readable.

I also have it set to use [recommonmark]() in case any one wants to use markdown really badly.

It also uses the default [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html) to insert links to the related source code.




## Local testing
You'll need the following python packages (and dependencies). From my command history getting it up and running;
```
git clone https://github.com/sebastiansam55/autokey-sphinx
cd autokey-sphinx
git clone https://github.com/autokey/autokey
cd autokey
pip install .
cd ..
pip install sphinx recommonmark sphinx-rtd-theme sphinx-epytext enum-tools[sphinx]
# for first time installs you'll likely have to restart your shell for the sphinx-build command to be found.

# should be run from the base of this repository
sphinx-build -a -E -b html . ./docs
```


## Github Actions
Basic workflow:
* Installs Git
* Clones autokey/autokey (master branch)
* Installs Autokey using `pip install .` in autokey repo
* Installs sphinx
    * `pip install sphinx recommonmark sphinx-rtd-theme sphinx-epytext`
* Builds sphinx site
    * `sphinx-build -a -E -b html ./ docs`
* Uploads pages Artifact (docs output folder)
* Deploys to Github Pages for this repository


## Maintenance of GitHub Actions
When a pull request is merged in, its action will need to be run manually to rebuild the documentation pages:
1. Pick one:
   * Navigate to the workflow:
     1. Open the [repository](https://github.com/autokey/autokey.github.io).
     2. Open the **Actions** menu.
     3. Choose **Build AutoKey pages** in the left pane.
   * Go directly to the workflow from here:
     1. Go to [Build Autokey pages](https://github.com/autokey/autokey.github.io/actions/workflows/pages.yml)
2. Click the **Run workflow** drop-down in the right pane.
3. Click the **Run workflow** button in the context menu.
4. Wait for the process to finish.
5. Open the [new documentation](https://autokey.github.io/index.html) and check if the change looks good or if further work is needed.


## TODO
There is a plugin that supports versioned documentation, [sphinxcontrib-multiversion](https://github.com/Holzhaus/sphinx-multiversion) which seems to be decently well maintained.

Going forward we should use sphinx syntax in comments instead of older epytext.;
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

For more information on the new comment markup.


