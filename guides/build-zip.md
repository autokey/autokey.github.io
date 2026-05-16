# Build a zip archive of the HTML documentation files
You can generate a zip file from the HTML documentation files as an archive that can be shared and used to access the documentation offline.
1. Update the system packages:
   ```bash
   sudo apt update
   ```
2. Install the core packages:
   ```bash
   sudo apt install -y git python3-pip python3-venv zip
   ```
3. Create the `**clones** directory:
   ```bash
   mkdir -p ~/clones
   ```
4. Change to the **clones** directory:
   ```bash
   cd clones
   ```
5. Clone the **AutoKey** and **AutoKey documentation** repositories as siblings in the current directory:
   ```bash
   git clone https://github.com/autokey/autokey.git && git clone https://github.com/autokey/autokey.github.io.git
   ```
6. Create a virtual environment:
   ```bash
   python3 -m venv --system-site-packages .venv
   ```
7. Activate the virtual environment (your prompt will change):
   ```bash
   source .venv/bin/activate
   ```
8. Change to the **AutoKey documentation** directory:
   ```bash
   cd autokey.github.io
   ```
9. Install the necessary dependencies:
   *(Note: pyasyncore, pyinotify, and python-xlib are required for modern Ubuntu builds)*
   ```bash
   pip install pyasyncore pyinotify python-xlib -r requirements.txt
   ```
10. Generate a fresh build of the documentation:
    ```bash
    make clean html
    ```
11. Verify the build by viewing the generated documentation in your browser:
    ```bash
    xdg-open _build/html/index.html 2>/dev/null
    ```
12. Create the zip archive from the HTML files:
    1. Extract the release version from the `conf.py` file:
       ```bash
       VERSION=$(python3 -c "import conf; print(conf.release)" | tail -n 1)
       ```
    2. Create the zip archive from inside the **html** folder, storing its contents at the root of the zip file and using the extracted version for the name:
       ```bash
       (cd _build/html && zip -r "../../autokey-docs_v${VERSION}.zip" .)
       ```
    3. Save the zip file to your home directory:
       ```bash
       mv autokey-docs_v*.zip ~/
       ```
13. Clean up afterwards:
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
* To use the archive, unzip it and open the `index.html` file. Note that the search bar and some local links may fail offline due to browser security restrictions.
