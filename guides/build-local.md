# Build the documentation locally
This is a stand-alone guide that provides the steps needed to build the documentation locally and create a folder of HTML files similar to the online documentation. It's intended to be used in a clean, new virtual machine with a fresh installation of **Ubuntu** in it.
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
5. Create the `~/clones` directory:
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
    pip install -r requirements.txt
    ```
12. Generate a fresh build of the HTML documentation:
     ```bash
     make clean html
     ```
13. Interpret the output:
    * You might see some warnings like these in the logs:
      * The **UserWarning: Container node skipped:** warning is just **recommonmark** (the **Markdown** parser) being a bit chatty. You can safely ignore it.
      * The **SyntaxWarning: invalid escape sequence '\+':** is a classic **Python 3.12+** warning. Somewhere in the AutoKey code, there’s a string (likely a Regex) using a backslash that isn't a "raw" string. It’s a tiny bug in the source code, but it won't break your documentation. It can be dealt with by using `r"""` on the offending docstring(s).
      * The **toctree:** warnings (for example, the one warning that the `CHANGELOG.md` file isn't in a **toctree**) means that there’s no link to that file in the main sidebar menu.
14. Get some visual proof that it worked by viewing the generated documentation in your browser:
    ```bash
    xdg-open _build/html/index.html 2>/dev/null
    ```
15. Clean up afterwards:
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
