# Autokey Documentation

## About this repository

### Resources
* Built using [Sphinx](https://github.com/sphinx-doc/sphinx).
* Uses the [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) extension to import the modules, read the documentation for each function, and automatically generate the API documentation based on that.
* Uses the [sphinx epytext](https://github.com/jayvdb/sphinx-epytext) extension to convert older-style Epydoc documentation format to Sphinx-readable documentation.
* Uses the [recommonmark](https://pypi.org/project/recommonmark/) package so that **Markdown** can be used.
* Uses the default [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html) to insert links to the related source code.

### Basic workflow
1. Clones the **master** branch of the [autokey/autokey](https://github.com/autokey/autokey) repository.
2. Installs **Autokey** in the cloned autokey repository.
3. Installs **Sphinx**.
4. Builds the **Sphinx** site in the **docs** folder.
5. Uploads the [GitHub Pages](https://pages.github.com/) from the **docs** folder.
6. Deploys the [documentation](https://autokey.github.io/index.html) as **GitHub Pages**.


### Local testing
1. You'll need the following Python packages and dependencies:
   ```bash
   # Clone the AutoKey documentation repository:
   git clone https://github.com/autokey/autokey.github.io.git
   # Open the AutoKey documentation cloned directory:
   cd autokey.github.io
   # Clone the Autokey repository:
   git clone https://github.com/autokey/autokey
   # Open the AutoKey cloned directory:
   cd autokey
   # Install Autokey in the cloned autokey repository:
   pip install .
   # Reopen the AutoKey documentation cloned directory
   cd ..
   # Install Sphinx and recommonmark:
   pip install sphinx recommonmark sphinx-rtd-theme sphinx-epytext enum-tools[sphinx]
   ```
2. If this is a first-time installation, restart the shell so that the `sphinx-build` command can be found, and reopen the AutoKey documentation cloned directory.
3. Build the documentation:
   ```bash
   # Build the Sphinx site:
   sphinx-build -a -E -b html . ./docs
   ```


## Maintenance

### Run the actions after documentation changes
When changes are made to the documentation, the GitHub actions will need to be run manually to rebuild the documentation pages:
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


### Update the actions
The GitHub action versions should be checked and updated regularly.
1. Check the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file on the **master** branch for updates:
   1. Check if the **actions/checkout** [version number has changed](https://github.com/marketplace/actions/checkout)
   2. Check if the **actions/upload-pages-artifact** [version number has changed](https://github.com/marketplace/actions/upload-github-pages-artifact).
   3. Check if the **actions/deploy-pages** [version number has changed](https://github.com/marketplace/actions/deploy-github-pages-site).
2. Update the version numbers if any have changed:
   1. Fork this repository. Note that GitHub will automatically open the fork that you just created.
   2. Create the **update_the_actions** branch off of the **master** branch. Note that GitHub will automatically put you onto the new branch that you just created.
   3. Open the **pages.yml** file.
   4. Update the version numbers of the actions that have changed.
   5. Save and commit the file.
   6. Update the change log:
      1. Open the **CHANGELOG.md** file.
      2. ️Note the change.
      3. ️Save and commit the file.
   7. ️Do a pull request.
   8. Do the cleanup:
         1. Wait for an email message notifying you that an administrator has merged the pull request into the project.
         2. Open the merged pull request by clicking its link in that email message.
         3. Click the **Delete branch** button.


### Update the dependencies
The pip dependencies should be checked and updated regularly.
1. Check the dependencies in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file on the **master** branch for updates:
   1. Check if the **sphinx** [version number has changed](https://pypi.org/project/Sphinx/).
   2. Check if the **sphinx_rtd_theme** [version number has changed](https://pypi.org/project/sphinx-rtd-theme/).
   3. Check if the **sphinx-epytext** [version number has changed](https://pypi.org/project/sphinx-epytext/).
   4. Check if the **recommonmark** [version number has changed](https://pypi.org/project/recommonmark/).
   5. Check if the **enum-tools[sphinx]** [version number has changed](https://pypi.org/project/enum-tools/).
2. Update the version numbers if any have changed:
   1. Fork this repository. Note that GitHub will automatically open the fork that you just created.
   2. Create the **update_the_dependencies** branch off of the **master** branch. Note that GitHub will automatically put you onto the new branch that you just created.
   3. Open the **requirements.txt** file.
   4. Update the version numbers of the dependencies that have changed.
   5. Save and commit the file.
   6. Update the change log:
      1. Open the **CHANGELOG.md** file.
      2. ️Note the change(s) you made.
      3. ️Save and commit the file.
   7. ️Do a pull request.
   8. Do the cleanup:
      1. Wait for an email message notifying you that an administrator has merged the pull request into the project.
      2. Open the merged pull request by clicking its link in that email message.
      3. Click the **Delete branch** button.

## ToDo
* Going forward, we should use **Sphinx** syntax in comments instead of the older **Epytext** syntax. See the [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for more information on the new comment markup.
* We should consider using the [sphinxcontrib-multiversion](https://github.com/Holzhaus/sphinx-multiversion) plugin that supports versioned documentation and seems to be decently well-maintained.
