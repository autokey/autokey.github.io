## Mock GitHub simulation
This is a stand-alone guide that provides the steps needed to verify that the `conf.py` file's logic works for both **local** and **GitHub CI** builds and tests by simulating a **GitHub** environment inside of a virtual machine. It's intended to be used in a clean, new virtual machine with a fresh installation of **Ubuntu** in it.

### Before you begin
On GitHub, the documentation and the source code often share a root directory rather than being siblings, as they are in a local environment.

This diagram shows the **local** development environment in which the **autokey** and **autokey.github.io** directories are **siblings** inside of the **clones** parent directory:
```
clones/                  (your local development workspace)
├── autokey.github.io/   (the cloned AutoKey documentation repository)
│   └── conf.py          (the conf.py file inside the Autokey.documentation repository)
└── autokey/             (the cloned AutoKey repository)
    └── lib/             (the lib sub-directory inside the AutoKey repository)
```

This diagram shows the **GitHub CI** development environment in which the **autokey** directory is a **child** of the **autokey.github.io** directory and the **autokey.github.io** directory is a **child** of the **clones** parent directory:
```
clones/                  (your local development workspace)
└── fake-github/         (the cloned AutoKey documentation repository)
    ├── conf.py          (the conf.py file inside the Autokey.documentation repository)
    └── autokey/         (the cloned Autokey repository)
        └── lib/         (the lib sub-directory inside the AutoKey repository)
```
By running the **tox** tests **locally** followed by running a build in a **GitHub** mock followed by one more round of running the **tox** tests **locally**, you can confirm, from the logs and from the placement of the resulting files, that the **os.path.exists** logic in the `conf.py` file correctly switches between the **sibling** folder (../autokey) and the internal **parent/child** folder (./autokey) based on its surroundings.

### 1. Run the tox tests
Use **tox** to run compatibility tests locally to ensure that your local copy of the AutoKey documentation passes the same checks used by the [GitHub CI workflow](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) before you push your changes to the repository:
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
5. Create the **clones** directory:
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
10. If the tests pass, view and inspect the test-output in your browser:
    1. Open the test output in your browser:
       ```bash
       xdg-open autokey.github.io/_build/html/index.html 2>/dev/null
       ```
    2. Navigate to the **API Reference** section.
    3. Check if the function names and descriptions are visible. If you see names, but no descriptions, or you encounter a **Module not found** error, verify that the **AutoKey** repository was cloned correctly into the `~/clones` directory.
11. To share the test results, copy the terminal output and paste it into a **GitHub** Markdown code-block or paste it into a file on your desktop or in your home directory for sharing later.

### 2. Do the GitHub mock
Mimic the directory structure that **Sphinx** encounters on the server, giving you full confidence before you push your local changes to the remote repository: 
1. Simulate the **GitHub** environment:
   
   1. You should still be in the **clones** directory from the previous tests. If you're not, enter the **clones** directory:
      ```bash
      cd ~/clones
      ```
   2. Create a **fake-github** sub-directory:
      ```bash
      mkdir fake-github/autokey
      ```
   3. Link the local repositories from the **clones** directory into the **fake-github** directory to mimic **GitHub**:
      ```bash
      cp -r autokey.github.io/* fake-github/
      cp -r autokey/* fake-github/autokey/
      ```
2. Run a mock-CI build from within that structure:
   1. Change to the **fake-github** directory:
      ```bash
      cd ~/clones/fake-github
      ```
   2. Borrow the **tox** environment so **Sphinx** can find your extensions (your prompt will change since you're now in a **tox** virtual environment):
      ```bash
      source ~/clones/.tox/docs/bin/activate
      ```
   3. Rename the original **autokey** directory to **autokey-hidden** so that **Sphinx** can't accidentally find it:
      ```bash
      mv ~/clones/autokey ~/clones/autokey-hidden
      ```
   4. Clear out old build to force a complete re-evaluation:
      ```bash
      rm -rf _build/
      ```
   5. Run a **Sphinx** build manually:
      ```bash
      sphinx-build -b html . _build/html
      ```
      or:
      ```bash
      make clean html
      ```
   6. Check the logs:
      * You should see **Sphinx Config: Using GitHub Actions path structure** near the beginning of the log.
   7. Rename the original **autokey-hidden** directory to **autokey** to restore it so that **Sphinx** can find it:
      ```bash
      mv ~/clones/autokey-hidden ~/clones/autokey
      ```
3. Run a final round of **tox** tests in the original **clones** directory to verify that your local development path still works:
   1. Go back to the **clones** directory:
      ```bash
      cd ~/clones
      ```
   2. Run the **tox** test:
      ```bash
      tox -r -e docs
      ```
   3. Check the logs:
      * You should see **Sphinx Config: Using local/tox path structure** near the beginning of the log.

### 3. Clean up the environment
1. Change out of the **clones** directory:
   ```bash
   cd
   ```
2. Remove the **clones** directory:
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
* Cross-platform testing: While this guide is written specifically for a clean **Ubuntu** virtual machine, developers are encouraged to test the documentation tools across different Linux distributions. If you choose to run these steps on other operating systems (like **Debian** or **Fedora**), you may want to run the `deactivate` command immediately after step 2.5 (running the manual Sphinx build) in the **Do the GitHub mock** section to drop your terminal out of the borrowed virtual environment and prevent potential environment-nesting or path conflicts during the final round of tests.
