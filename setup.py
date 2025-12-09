from setuptools import setup, find_packages
import os

os.environ.setdefault("MY_PACKAGE_SETTING", "default_value")    

install_requires = [
    # Core
    "numpy>=1.19.5",
    "pandas>=1.1.5",
    "matplotlib>=3.3.4",

    # ML / DL
    "scikit-learn>=1.0.0",
    "tensorflow>=2.10.0",

    # Reinforcement Learning
    "gym>=0.26.0",
    "gymnasium>=0.29.0",
    "stable-baselines3>=2.0.0",

    # Visualization + utils
    "seaborn>=0.11.1",
    "tqdm>=4.60.0",
    "opencv-python>=4.5.0",
]

extras = {
    "rl": [
        "gym[box2d]",
        "ale-py",
        "pygame",
        "shimmy",
    ],
    "dev": [
        "black",
        "flake8",
        "pytest",
        "mypy",
    ],
}

setup(
    name="scripting_practice",
    version="0.1.2",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras,
    python_requires=">=3.9",
    author="ducanh19082007",
    include_package_data=True,
)
