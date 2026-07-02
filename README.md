# AutoKey Documentation

### About this repository
This is the repository that builds the [AutoKey documentation](https://autokey.github.io/index.html). If you're a user looking for help with **AutoKey**, see the [AutoKey](https://github.com/autokey/autokey) repository. If you have suggestions for how the documentation can be improved, please create an [issue](https://github.com/autokey/autokey.github.io/issues) to let us know about them. <!-- TODO: If you'd like to help build or maintain the documentation, please see the [CONTRIBUTORS.md](https://github.com/autokey/autokey.github.io/blob/master/CONTRIBUTORS.md) file. -->

### Resources
* Built using the [Sphinx](https://github.com/sphinx-doc/sphinx) Python documentation-generator to build the HTML **AutoKey** documentation files.
* Uses the [recommonmark](https://pypi.org/project/recommonmark/) package so that **Markdown** can be used.
* Uses the [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) extension to import the modules, read the documentation for each function, and automatically generate the API documentation from that.
* Uses the [sphinx epytext](https://github.com/jayvdb/sphinx-epytext) extension to convert older-style **Epydoc** documentation format to **Sphinx**-readable documentation.
* Uses the default [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html) extension to insert links to the related source-code.

### Basic workflows
* **Local workflow**:
  * The steps you can take to build and preview the documentation locally:
    1. Clone your fork of the [AutoKey documentation](https://github.com/autokey/autokey.github.io) repository.
    2. Clone the **master** branch of the [AutoKey](https://github.com/autokey/autokey) repository into the same directory **next to** the **AutoKey documentation** clone so that **Sphinx** can read its Python docstrings.
    3. Install the the project's required dependencies.
    4. Run the local build command. The configuration script will automatically detect the sibling path-structure and compile your documentation in the default automatically-created `_build` directory.
    5. Open `_build/html/index.html` in your browser to verify your visual layout changes.
* **Remote workflow**:
  * The steps GitHub takes to build and deploy the documentation:
    1. Clones the **master** branch of the [AutoKey documentation](https://github.com/autokey/autokey.github.io) repository.
    2. Clones the **master** branch of the [AutoKey](https://github.com/autokey/autokey) repository **inside of** the **AutoKey documentation** directory so that **Sphinx** can read its Python docstrings.
    3. Installs the project's required dependencies.
    4. Builds the **Sphinx** site in the **docs** directory, which it automatically creates inside of the **AutoKey documentation** directory. Note that the `docs` directory is used here instead of the default `_build` directory so that [GitHub Pages](https://docs.github.com/en/pages) can find the files.
    5. Uploads the [GitHub Pages](https://docs.github.com/en/pages) deployment package from the **docs** folder.
    6. Deploys the live [documentation](https://autokey.github.io/index.html) as **GitHub Pages**.
    7. Visit the [AutoKey documentation](https://autokey.github.io/index.html) page to see the changes.

### Developer and maintenance guides
Several guides are available to provide technical procedures for maintaining the documentation and repository:
* [Audit links](https://github.com/autokey/autokey.github.io/blob/master/guides/audit-links.md) - Check link integrity and manage URL exceptions in the documentation.
* [Build local documentation](https://github.com/autokey/autokey.github.io/blob/master/guides/build-local.md) - Generate the documentation locally and preview the changes.
* [Build PDF archives](https://github.com/autokey/autokey.github.io/blob/master/guides/build-pdf.md) - Generate PDF archives of the documentation for sharing.
* [Build zip archives](https://github.com/autokey/autokey.github.io/blob/master/guides/build-zip.md) - Generate zipped archives of the HTML documentation for sharing.
* [Manual documentation rebuild](https://github.com/autokey/autokey.github.io/blob/master/guides/rebuild-site.md) - Trigger a live documentation update.
* [Run local tests](https://github.com/autokey/autokey.github.io/blob/master/guides/test-local.md) - Run local **tox** compatibility tests on the documentation.
* [Simulate the GitHub environment](https://github.com/autokey/autokey.github.io/blob/master/guides/mock-github.md) - Create a mock GitHub environment to test if local and remote builds will work.
* [Update GitHub Actions](https://github.com/autokey/autokey.github.io/blob/master/guides/bump-actions.md) - Maintain action and security versions.
* [Update dependencies](https://github.com/autokey/autokey.github.io/blob/master/guides/bump-dependencies.md) - Keep Python packages up-to-date.
* [Update guides](https://github.com/autokey/autokey.github.io/blob/master/guides/bump-references-in-guides.md) - Keep the version references in the guides up-to-date.

### ToDo
* Upgrade this repository to use **Sphinx** syntax instead of the older **Epytext** syntax. See the [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for more information on the new markup.
* Consider using the [sphinxcontrib-multiversion](https://github.com/Holzhaus/sphinx-multiversion) plugin that supports versioned documentation and seems to be decently well-maintained.
* Move this section to the `CONTRIBUTORS.md` file once it exists.
