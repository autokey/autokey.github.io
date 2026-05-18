# Build a zip archive of the HTML documentation files
This is a stand-alone guide that uses **Sphinx** (the Python documentation generator) to build the AutoKey HTML documentation files locally and generates a fully-searchable zip file from them that can be shared and used to access the documentation offline. The guide is intended to be used in a clean, new virtual machine with a fresh installation of **Ubuntu** in it.
1. Boot into a fresh copy of **Ubuntu 22.04** or **Ubuntu 24.04** in a new virtual machine.
2. Open a terminal window.
3. Update the system packages:
   ```bash
   sudo apt update
   ```
4. Install the core packages:
   ```bash
   sudo apt install -y git python3-pip python3-venv zip
   ```
5. Create the `**clones** directory:
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
10. Change to the **AutoKey documentation** directory:
    ```bash
    cd autokey.github.io
    ```
11. Install the necessary dependencies:
    ```bash
    pip install pyasyncore pyinotify python-xlib -r requirements.txt
    ```
12. Check the links in the documentation before doing the build:
    1. Check the validity of the links in the documentation:
       ```bash
       make linkcheck
       ```
    2. If there are errors, follow the suggestions **Sphinx** provides in the output for fixing them.
13. Generate a fresh build of the documentation:
    ```bash
    make clean html
    ```
14. Verify the build by viewing the generated documentation in your browser:
    ```bash
    xdg-open _build/html/index.html 2>/dev/null
    ```
15. Create the zip archive from the HTML files:
    1. Extract the release version from the `conf.py` file:
       ```bash
       VERSION=$(python3 -c "import conf; print(conf.release)" | tail -n 1)
       ```
    2. Create the zip archive of the contents of the **_build/html** folder and use the extracted version to name the file:
       ```bash
       tar -caf "autokey-docs_v${VERSION}.zip" -C _build/html .
       ```
    3. Save the zip file to your home directory:
       ```bash
       mv autokey-docs_v*.zip ~/
       ```
16. Clean up afterwards:
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
* Interpret the output:
  * You may see some warnings, like these, in the log:
    * The **UserWarning: Container node skipped:** warning is just **recommonmark** (the **Markdown** parser) being a bit chatty. You can safely ignore it.
    * The **SyntaxWarning: invalid escape sequence '\+':** is a classic **Python 3.12+** warning. Somewhere in the AutoKey code, there’s a string (likely a Regex) using a backslash that isn't a "raw" string. It’s a tiny bug in the source code, but it won't break your documentation. It can be dealt with by using `r"""` on the offending docstring(s).
    * The **toctree:** warnings (for example, the one warning that the `CHANGELOG.md` file isn't in a **toctree**) means that there’s no link to that file in the main sidebar menu.
* The **Sphinx** standardized directory structure is used in the zipped file:
  ```text
  autokey-docs_v[VERSION].zip
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
* To use the archive, unzip it and open the `index.html` file inside of the unzipped directory. Note that the search bar and some local links may fail offline due to browser security-restrictions.
