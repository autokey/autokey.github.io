# Autokey Documentation
* Built using [sphinx](https://github.com/sphinx-doc/sphinx).
* Uses the [sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) extension to automatically generate API documentation. This module imports the modules, reads the documentation for each function, and generates the API documentation based on that.
* Uses the [sphinx epytext](https://github.com/jayvdb/sphinx-epytext) extension to convert older-style Epydoc documentation format to Sphinx-readable documentation.
* Uses [recommonmark](https://pypi.org/project/recommonmark/) in case anyone wants to use Markdown.
* Uses the default [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html) to insert links to the related source code.


## Local testing
You'll need the following Python packages (and dependencies) to get it up and running;
```bash
git clone https://github.com/sebastiansam55/autokey-sphinx
cd autokey-sphinx
git clone https://github.com/autokey/autokey
cd autokey
pip install .
cd ..
pip install sphinx recommonmark sphinx-rtd-theme sphinx-epytext enum-tools[sphinx]
# For first time installs, you'll likely have to restart your shell for the sphinx-build command to be found.

# Should be run from the base of this repository:
sphinx-build -a -E -b html . ./docs
```


## About GitHub actions
Basic workflow:
* Installs Git
* Clones autokey/autokey (master branch)
* Installs Autokey using `pip install .` in the autokey repository
* Installs Sphinx
    * `pip install sphinx recommonmark sphinx-rtd-theme sphinx-epytext`
* Builds the Sphinx site
    * `sphinx-build -a -E -b html ./ docs`
* Uploads the Pages artifact (docs output folder)
* Deploys to GitHub Pages for this repository


## Run GitHub actions after documentation changes
When a pull request is merged in, its action will need to be run manually to rebuild the documentation pages:
1. Pick one:
   * Navigate to the workflow:
     1. Open the [repository](https://github.com/autokey/autokey.github.io).
     2. Open the **Actions** menu.
     3. Choose **Build AutoKey pages** in the left pane.
   * Go directly to the workflow from here:
     1. Go to [Build Autokey pages](https://github.com/autokey/autokey.github.io/actions/workflows/pages.yml).
2. Click the **Run workflow** drop-down in the right pane.
3. Click the **Run workflow** button in the context menu.
4. Wait for the process to finish.
5. Open the [new documentation](https://autokey.github.io/index.html) and check if the change looks good or if further work is needed.


## Update this repository
### Update the dependencies
The pip dependencies should be checked and updated regularly.
1. Check the dependencies in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file for updates:
   1. Check if the **sphinx==** [version number has changed](https://pypi.org/project/Sphinx/).
   2. Check if the **sphinx_rtd_theme==** [version number has changed](https://pypi.org/project/sphinx-rtd-theme/).
   3. Check if the **sphinx-epytext==** [version number has changed](https://pypi.org/project/sphinx-epytext/).
   4. Check if the **recommonmark==** [version number has changed](https://pypi.org/project/recommonmark/).
   5. Check if the **enum-tools[sphinx]==** [version number has changed](https://pypi.org/project/enum-tools/).
2. Update the version numbers if any have changed:
   1. Create the **update_the_dependencies** branch off of the **master** branch.
   2. Change to the **update_the_dependencies** branch.
   3. Open the `requirements.txt` file on the **update_the_dependencies** branch.
   4. Update the version numbers of the dependencies that have changed.
2. If you made changes:
   1. Save the `requirements.txt` file.
   2. Commit the file with this title:
      ```
      Update requirements.txt to bump dependency versions.
      ```
   3. Update the CHANGELOG:
      1. Open the `CHANGELOG.md` file on the **update_the_dependencies** branch.
      2. ️Note the change to the dependency file:
         ```
         * Bump dependency versions in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file.
         ```
      3. ️Save the `CHANGELOG.md` file.
      4. Commit the file with this title:
         ```
         Update CHANGELOG.md with bump to dependency versions.
         ```
   4. ️Do a pull request with this title:
      ```
      Bump dependency versions.
      ```
   5. Delete the **update_the_dependencies** branch once the pull request has been merged in.

### Update the GitHub actions
The GitHub action versions should be checked and updated regularly.
1. Check the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file on the **master** branch for updates:
   1. Check if the **uses: actions/checkout@** [version number has changed](https://github.com/marketplace/actions/checkout)
   2. Check if the **uses: actions/upload-pages-artifact@** [version number has changed](https://github.com/marketplace/actions/upload-github-pages-artifact).
   3. Check if the **uses: actions/deploy-pages@** [version number has changed](https://github.com/marketplace/actions/deploy-github-pages-site).
2. Update the version numbers if any have changed:
   1. Create the **update_the_actions** branch off of the **master** branch.
   2. Change to the **update_the_actions** branch.
   3. Open the `pages.yml` file on the **update_the_actions** branch.
   4. Update the version numbers of the actions that have changed.
3. If you made changes:
   1. Save the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file.
   2. Commit the file with this title:
      ```
      Update pages.yml to bump GitHub action versions.
      ```
   3. Update the CHANGELOG:
      1. Open the `CHANGELOG.md` file on the **update_the_actions** branch.
      2. ️Note the change to the workflow file:
         ```
         * Bump GitHub action versions in the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file.
         ```
      3. ️Save the `CHANGELOG.md` file.
      4. Commit the file with this title:
         ```
         Update CHANGELOG.md with bump to GitHub action versions.
         ```
   4. ️Do a pull request with this title:
      ```
      Bump GitHub action versions.
      ```
   5. Delete the **update_the_actions** branch once the pull request has been merged in.


## TODO
* There is the [sphinxcontrib-multiversion](https://github.com/Holzhaus/sphinx-multiversion) plugin that supports versioned documentation and it seems to be decently well-maintained.
* Going forward, we should use Sphinx syntax in comments instead of older Epytext. See https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html for more information on the new comment markup.
