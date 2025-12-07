from setuptools import setup, find_packages
import os

os.environ.setdefault("MY_PACKAGE_SETTING", "default_value")    

install_requires = [
    "requests>=2.25.1",
    "numpy>=1.19.5",
    "pandas>=1.1.5",
    "matplotlib>=3.3.4",
    "seaborn>=0.11.1",
]


extras = {
    "jupyter": [
        "notebook",
        "jupyterlab",
        "ipywidgets",
        "jupyterlab_widgets",
        "ipykernel",
    ],
    "dev": [
        "black",
        "flake8",
        "pytest",
        "pytest-cov",
        "mypy",
        "isort",
    ],
    "codespaces": [
        "ipykernel",
        "jedi",
        "debugpy",
        "jupyterlab",
        "notebook",
        "rich",
    ],
    "full": [
        "opencv-contrib-python",
        "albumentations",
        "imgaug",
        "seaborn",
        "tqdm",
    ],
}

setup(
    name="scripting_practice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras,
    python_requires=">=3.7",
    author="ducanh19082007",
    include_package_data=True,
)