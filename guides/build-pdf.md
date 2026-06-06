# Build a local PDF archive
This is a stand-alone guide that provides the steps needed to generate a single-file, fully searchable PDF version of the documentation using the **SimplePDF** extension for **Sphinx**. The guide is intended to be used in a clean, new virtual machine with a fresh installation of **Ubuntu** in it.
1. Boot into a fresh copy of **Ubuntu 22.04** or **Ubuntu 24.04** in a new virtual machine.
2. Open a terminal window.
3. Update the system packages:
   ```bash
   sudo apt update
   ```
4. Install the core packages:
   ```bash
   sudo apt install -y git python3-pip python3-venv python3-xlib
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
10. Change to the **AutoKey documentation** directory:
    ```bash
    cd autokey.github.io
    ```
11. Install the necessary dependencies:
    ```bash
    pip install pyinotify sphinx-simplepdf -r requirements.txt
    ```
12. Generate a fresh PDF file:
    ```bash
    make clean simplepdf
    ```
13. Move the generated PDF file to the home directory so it isn't deleted on clean-up:
    ```bash
    mv _build/simplepdf/autokey-docs-*.pdf ~/
    ```
14. Clean up afterwards:
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
* The PDF uses a traditional print layout with a **Table of Contents** rather than a sidebar.
* The PDF is styled with custom CSS from the repository's `_static` directory.
* Code blocks keep their syntax highlighting and images are embedded directly. 
* The PDF file does not contain the **Indices and Tables** section at the end.
* This guide defaults to building the PDF archive of the documentation locally from the **master** branch. Depending on your needs, choose one of these options for the **AutoKey** clone in **step 7** above:
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
