from setuptools import setup, find_packages
import os

os.environ.setdefault("MY_PACKAGE_SETTING", "default_value")    

install_requires = [
    "requests>=2.25.1",
    "numpy>=1.19.5",
    "pandas>=1.1.5",
    "scipy>=1.5.4",
    "matplotlib>=3.3.4",
    "scikit-learn>=0.24.1",
    "tqdm>=4.56.0",
    "yfinance>=0.1.63",
    "beautifulsoup4>=4.9.3",
    "pytest>=6.2.1",
    "pytest-cov>=2.11.1",
    "setuptools>=50.3.2",
    "seaborn>=0.11.1",
    "sklearn-pandas>=2.0.0",
    "scikit-learn>=0.24.1",
    "tensorflow>=2.4.1",
    "keras>=2.4.3",
    "torch>=1.7.1",
    "torchvision>=0.8.2",
    "transformers>=4.3.3",
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
    version="0.1.1",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras,
    python_requires=">=3.7",
    author="ducanh19082007",
    include_package_data=True,
)