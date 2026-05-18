# Bump the dependencies
The documentation repository's dependencies should be checked and updated regularly.
1. Check for updates:
   * Review the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file on the **master** branch and compare current versions against the latest releases on PyPI:
     * [dbus-python](https://pypi.org/project/dbus-python/)
     * [enum-tools[sphinx]](https://pypi.org/project/enum-tools/)
     * [recommonmark](https://pypi.org/project/recommonmark/)
     * [sphinx](https://pypi.org/project/Sphinx/)
     * [sphinx-epytext](https://pypi.org/project/sphinx-epytext/)
     * [sphinx_rtd_theme](https://pypi.org/project/sphinx-rtd-theme/)
     * [sphinx-toolbox](https://pypi.org/project/sphinx-toolbox/)
2. Apply available updates on GitHub:
   1. Fork the repository.
   2. Create a new branch named **update_dependencies** off of the **master** branch.
   3. Edit the dependencies:
      1. Open the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file in the GitHub editor.
      2. Click the **Edit** button.
      3. Update the version numbers that have changed (e.g., change **sphinx==7.1.2** to **sphinx==7.2.6**).
      4. Commit the change.
   4. Update change log:
      1. Open the [CHANGELOG.md](https://github.com/autokey/autokey.github.io/blob/master/CHANGELOG.md) file in the GitHub editor.
      2. Click the **Edit** button.
      3. Document the version bumps.
      4. Commit the change.
3. Submit a pull request:
   1. Open a pull request against the **master** branch of the repository.
4. Post-merge cleanup:
   1. Once an administrator merges the pull request:
      1. Open the merged pull request.
      2. Click the **Delete branch** button to keep your fork tidy.
      3. Synchronize the **master** branch in your fork to incorporate the change.
