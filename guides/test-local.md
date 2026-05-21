# Run local compatibility tests on the documentation
This stand-alone guide provides the steps needed to use **tox** to run local compatibility and build tests to ensure that your AutoKey documentation passes the same checks used by the GitHub CI pipeline before you push changes to the repository. It's intended for use in a clean virtual machine with a fresh installation of **Ubuntu** in it.
1. Boot into a fresh copy of **Ubuntu 22.04** or **Ubuntu 24.04** in a new virtual machine.
2. Open a terminal window.
3. Update the system packages:
   ```bash
   sudo apt update
   ```
4. Install the core packages:
   ```bash
   sudo apt install -y git libdbus-1-dev libglib2.0-dev pkg-config tox
   ```
5. Create the `~/clones` directory:
   ```bash
   mkdir ~/clones
   ```
6. Change to the **clones** directory:
   ```bash
   cd ~/clones
   ```
7. Clone the **AutoKey** and **AutoKey documentation** repositories:
   ```bash
   git clone https://github.com/autokey/autokey.git && git clone https://github.com/autokey/autokey.github.io.git
   ```
8. Copy the `tox.ini` file into the current directory:
   ```bash
   cp autokey.github.io/tox.ini .
   ```
9. Run the tests:
   ```bash
   tox -r -e docs
   ```
   * Interpret the output:
     * You may see some warnings:
       * **Container node skipped** warning: You can safely ignore this. It's a known issue with the older **Markdown** parser and does not affect the build quality.
       * **display_version** warning: You can safely ignore this. It's a theme-setting conflict that prevents the program's version-number from appearing under the logo in the sidebar.
       * **invalid escape sequence** warnings: You can safely ignore these. They're **Python 3.12** being strict about regex strings (expecting `r'[\w]'` instead of `'[\w]')`. Since these are in the **AutoKey** repo and not your documentation, they don't affect the build.
   * If the tests don't pass, make changes and re-run the tests, but remove the previous build-artifacts first:
     ```bash
     rm -rf autokey.github.io/_build/
     ```
11. If the tests pass, view and inspect the test-output in your browser:
    1. Open the test output in your browser:
       ```bash
       xdg-open autokey.github.io/_build/html/index.html 2>/dev/null
       ```
    2. Navigate to the **API Reference** section.
    3. Check if the function names and descriptions are visible. If you see names, but no descriptions, or you encounter a **Module not found** error, verify that the **AutoKey** repository was cloned correctly into the `~/clones` directory.
12. To share the test results, copy the terminal output and paste it into a GitHub Markdown code-block or paste it into a file on your desktop or in your home directory for sharing later.
13. Clean up the environment:
    1. Deactivate the **tox** virtual environment:
       ```bash
       deactivate
       ```
    2. Change out of the **clones** directory:
       ```bash
       cd
       ```
    3. Remove the **clones** directory:
       ```bash
       rm -rf ~/clones
       ```

### Notes
* This guide defaults to building the documentation locally from the **master** branch before testing it. Depending on your needs, choose one of these options for the **AutoKey** clone in **step 7** above:
  * Clone the **develop** branch:
    ```bash
    git clone --branch develop --single-branch https://github.com/autokey/autokey.git
    ```
  * Clone the **master** branch (current release):
    ```bash
    git clone https://github.com/autokey/autokey.git
    ```
  * Clone a specific **pull request** (replace **123** with the target pull request number):
    ```bash
    PR=123; git clone https://github.com/autokey/autokey.git && (cd autokey && git fetch origin pull/$PR/head:pull_$PR && git checkout pull_$PR)
    ```
