# Changelog

## Version 0.97.0~beta0
<!-- ⬇️ ALWAYS INSERT NEW BULLETED ITEMS DIRECTLY BELOW THIS LINE ⬇️ -->
- Add deactivation of the **tox** virtual environment to the cleanup steps in the [test-local.md](https://github.com/autokey/autokey.github.io/blob/master/guides/test-local.md) file.
- Add a guide for running **tox** tests on a local copy of the documentation.
- Add a guide for building a tarball archive of the HTML documentation.
- Make necessary changes to the [build-zip.md](guides/build-zip.md) guide.
- Add  clone options to the [build-pdf.md](https://github.com/autokey/autokey.github.io/blob/master/guides/build-pdf.md) guide.
- Add  clone options to the [build-local.md](https://github.com/autokey/autokey.github.io/blob/master/guides/build-local.md) guide.
- Migrate [dependencies update procedure](https://github.com/autokey/autokey.github.io/blob/master/README.md#update-the-dependencies) to a stand-alone guide.
- Migrate [update actions procedure](https://github.com/autokey/autokey.github.io/blob/master/README.md#update-the-actions) to a stand-alone guide.
- Remove the no-longer-needed `.gitignore` file from the `_static` directory.
- Reorganize the [CHANGELOG.md](https://github.com/autokey/autokey.github.io/blob/master/CHANGELOG.md) file.
- Add a guide for building a zip archive of the HTML documentation.
- Add a guide for building local PDF documentation.
- Make corrections to the `build-local.md` file for clarity and accuracy.
- Add the **custom.css** file to the **_static** directory and populate it with a selector combination for styling PDF archives of the documentation.
- Update Sphinx and other dependencies in the `requirements.txt` file.
- Add the missing **_static** directory and populate it with the empty `.gitkeep` file as a temporary placeholder.
- Add the `tox.ini` configuration file for use in testing.
- Update configuration for **Sphinx** documentation builder by adding the **SimplePDF** extension, enhancing path-logic, and isolating local and remote build environments.
- Refactor the `index.rst` file to include the **Indices and Tables** section only in HTML builds.
- Update the `pages.yml` workflow to modernize system-header build dependencies and add support for **dbus**.
- Clean up prior development artifact from the `.gitignore` file and add **tox** exclusion.
- Add a guide for local HTML documentation builds and remove the temporary `.gitkeep` file from the directory.
- Add new **guides** directory with the empty `.gitkeep` file in it as a temporary placeholder.
- Revert the version bump to **sphinx** in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file.
- Bump versions in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file.
- Update the [CHANGELOG.md](https://github.com/autokey/autokey.github.io/blob/master/CHANGELOG.md) file to include AutoKey versions and date-stamps.
- Bump GitHub actions in the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file.

## Version 0.96.0
- Fix invalid indentation in the [api.rst](https://github.com/autokey/autokey.github.io/blob/master/api.rst) file.
- Fix invalid syntax in the [intro.rst](https://github.com/autokey/autokey.github.io/blob/master/intro.rst) file.
- Bump **sphinx** and **enum-tools** versions in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file.
- Fix broken link in the [intro.rst](https://github.com/autokey/autokey.github.io/blob/master/intro.rst) file.
- Bump action versions in the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file.
- Update all sections in the [README.md](https://github.com/autokey/autokey.github.io/blob/master/README.md) file and add a section.
- Bump dependency versions in the [requirements.txt](https://github.com/autokey/autokey.github.io/blob/master/requirements.txt) file.
- Update the "Maintenance of GitHub Actions" section in the [README.md](https://github.com/autokey/autokey.github.io/blob/master/README.md) file.
- Add the "Maintenance of GitHub Actions" section to the [README.md](https://github.com/autokey/autokey.github.io/blob/master/README.md) file.
- Add this file.
