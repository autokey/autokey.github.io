# Build a compressed tarball archive of the HTML documentation files
This is a stand-alone guide that uses **Sphinx** (the Python documentation generator) to build the AutoKey HTML documentation files locally and generates a compressed tarball file from them that can be shared and used to access the documentation offline. The guide is intended to be used in a clean, new virtual machine with a fresh installation of **Ubuntu** in it.
1. Boot into a fresh copy of **Ubuntu 22.04** or **Ubuntu 24.04** in a new virtual machine.
2. Open a terminal window.
3. Update the system packages:
   ```bash
   sudo apt update
   ```
4. Install the core packages:
   ```bash
   sudo apt install -y git python3-pip python3-venv
   ```
5. Create the **clones** directory:
   ```bash
   mkdir ~/clones
   ```
6. Change to the **clones** directory:
   ```bash
   cd ~/clones
   ```
7. Clone the **AutoKey** and **AutoKey documentation** repositories as siblings in the current directory:
   ```bash
   git clone https://github.com/autokey/autokey.git && git clone https://github.com/autokey/autokey.github.io.git
   ```
8. Create a virtual environment:
   ```bash
   python3 -m venv --system-site-packages .venv
   ```
9. Activate the virtual environment (your prompt will change):
   ```bash
   source .venv/bin/activate
   ```
10. Navigate to the documentation directory:
    ```bash
    cd autokey.github.io
    ```
11. Install the core packages:
    ```bash
    pip install pyasyncore pyinotify python-xlib -r requirements.txt
    ```
12. Check the links in the documentation before doing the build:
    1. Check the validity of the links in the documentation:
       ```bash
       make linkcheck
       ```
    2. If there are errors, follow the suggestions **Sphinx** provides in the output for fixing them.
13. Generate a fresh, local build of the documentation:
    ```bash
    make clean html
    ```
14. Preview the built documentation in your browser:
    ```bash
    xdg-open _build/html/index.html 2>/dev/null
    ```
15. Create the tarball from the documentation:
    1. Fetch the **AutoKey** version identifier:
       ```bash
       VERSION=$(python3 -Bc "import conf; print(conf.release)" | tail -n 1)
       ```
    2. Navigate to the `_build/html` directory:
       ```bash
       cd _build/html
       ```
    3. Create the versioned tarball:
       ```bash
       tar -czvf ~/autokey-docs-${VERSION}.tar.gz *
       ```
16. Verify that the **tarball** is good:
    * Check the file-count (there should be 2 more files in the source directory than in the **tarball**):
      1. Navigate to your home directory:
         ```bash
         cd
         ```
      2. Check the file-count of the source directory:
         ```bash
         find ~/clones/autokey.github.io/_build/html | wc -l
         ```
      3. Check the file-count in the **tarball**:
         ```bash
         tar -tf autokey-docs-*.tar.gz | wc -l
         ```
    * Check the integrity of the **tarball**:
      ```bash
      tar -tf autokey-docs-*.tar.gz > /dev/null && echo "OK" || echo "CORRUPTED"
      ```
    * Check the archive layout and contents without extracting them:
      ```bash
      tar -tf autokey-docs-*.tar.gz
      ```
17. Clean up afterwards:
    1. Deactivate the virtual environment:
       ```bash
       deactivate
       ```
    2. Leave the **clones** directory:
       ```bash
       cd
       ```
    3. Remove the **clones** directory:
       ```bash
       rm -rf ~/clones/
       ```

### Notes:
* Interpret the build output:
  * You may see some warnings, like these, in the log when building the documentation:
    * The **UserWarning: Container node skipped:** warning is just **recommonmark** (the **Markdown** parser) being a bit chatty. You can safely ignore it.
    * The **SyntaxWarning: invalid escape sequence '\+':** is a classic **Python 3.12+** warning. Somewhere in the AutoKey code, there’s a string (likely a Regex) using a backslash that isn't a "raw" string. It’s a tiny bug in the source code, but it won't break your documentation. It can be dealt with by using `r"""` on the offending docstring(s).
    * The **toctree:** warnings (for example, the one warning that the `CHANGELOG.md` file isn't in a **toctree**) means that there’s no link to that file in the main sidebar menu.
* The 2-file discrepancy between the number of files in the source directory and the **tarball** is expected because the shell wildcard used during compression ignores the single-dot (.) root directory and the hidden **Sphinx** `.buildinfo` artifact file.
* The **tarball** will contain the **Sphinx** standardized directory structure:
  ```text
  autokey-docs-[VERSION].tar.gz
  ├── api/
  ├── _modules/
  ├── _sources/
  ├── _static/
  ├── index.html
  └── [other root .html files]
  ```
  * The **api** subdirectory contains the generated **HTML** pages for the project's **API** code references.
  * The **_modules** sub-directory contains syntax-highlighted **HTML** copies of the **Python** source-code modules.
  * The **_sources** sub-directory contains the raw, uncompiled **reStructuredText (.rst)** or **Markdown (.md)** files used for building each page.
  * The **_static** sub-directory contains stylesheet assets, like **CSS**, **JavaScript** files, fonts, and graphics used for rendering the layout.
* This guide defaults to building the documentation locally from the **master** branch. Depending on your needs, choose one of these options for the **AutoKey** clone in **step 7** above:
  * Clone the **develop** branch:
    ```bash
    git clone --branch develop --single-branch https://github.com/autokey/autokey.git
    ```
  * Clone the **master** branch (current release):
    ```bash
    git clone https://github.com/autokey/autokey.git
    ```
  * Clone a **pull request**, replacing **123** with the pull request number:
    ```bash
    PR=123; git clone https://github.com/autokey/autokey.git && (cd autokey && git fetch origin pull/$PR/head:pull_$PR && git checkout pull_$PR)
    ```
  * To use the archive, unpack it by double-clicking it in your file manager or with the `tar -xvf autokey-docs-[VERSION].tar.gz` command (replacing VERSION with the actual version) and open the `index.html` file inside of the unpacked directory. Note that the search bar and some local links may fail offline due to browser security-restrictions.
