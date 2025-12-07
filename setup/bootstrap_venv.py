import os
import subprocess
import sys
import platform

VENV_DIR = "venv"
GITIGNORE_FILE = ".gitignore"

def venv_python(venv_dir = VENV_DIR):
    if venv_dir == "":
        venv_dir = VENV_DIR
    if platform.system() == "Windows":
        return os.path.join(venv_dir, "Scripts", "python.exe")
    return os.path.join(venv_dir, "bin", "python")



def venv_pip(venv_dir = VENV_DIR):
    if venv_dir == "":
        venv_dir = VENV_DIR
    if platform.system() == "Windows":
        return os.path.join(venv_dir, "Scripts", "pip")
    return os.path.join(venv_dir, "bin", "pip")




def ensure_gitignore(venv_dir = VENV_DIR):
    if venv_dir == "":
        venv_dir = VENV_DIR
    print("\n Ensuring .gitignore has venv excluded...")

    # Create .gitignore if missing
    if not os.path.exists(GITIGNORE_FILE):
        with open(GITIGNORE_FILE, "w") as f:
            f.write(f"{venv_dir}\n")
        print(f" Added {venv_dir}/ to new .gitignore")
        return
    # Check if the given venv already listed
    with open(GITIGNORE_FILE, "r") as f:
        rules = f.read()

    if "{venv_dir}/" not in rules:
        with open(GITIGNORE_FILE, "a") as f:
            f.write(f"\n{venv_dir}/\n")
        print(f" Added {venv_dir} to .gitignore")
    else:
        print(f" {venv_dir} already ignored")
    # Remove from git tracking if already tracked
    try:
        subprocess.run(["git", "rm", "-r", "--cached", venv_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f" Removed {venv_dir} from Git cache (if tracked before)")
    except FileNotFoundError:
        print(" Git not available, skipping cache cleanup")



def create_venv(venv_dir = VENV_DIR):
    if venv_dir == "":
        venv_dir = VENV_DIR
    if not os.path.exists(venv_dir):
        print("\n Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    else:
        print("\n Virtual environment already exists")



def install_editable_package(venv_dir=VENV_DIR):
    if venv_dir == "":
        venv_dir = VENV_DIR

    py = venv_python(venv_dir)

    print("\nUpgrading pip + setuptools + wheel...")
    subprocess.check_call([py, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    print("\nInstalling package in editable mode (-e .)...")
    subprocess.check_call([py, "-m", "pip", "install", "-e", "."])


def main(venv_dir):
    if venv_dir == "":
        venv_dir = VENV_DIR
    ensure_gitignore(venv_dir)
    create_venv(venv_dir)
    install_editable_package(venv_dir)

    print("\n Environment setup complete!")
    print("\n Activate the environment:")
    if platform.system() == "Windows":
        print(f" {venv_dir}\\Scripts\\activate")
    else:
        print(f" source {venv_dir}/bin/activate")



if __name__ == "__main__":
    venv_dir = input("input your virtual environment name here: ") #without .
    main(venv_dir)