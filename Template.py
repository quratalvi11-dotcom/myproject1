import os
from pathlib import Path

package_name = "dataquick"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/analyzer.py",
    f"src/{package_name}/visualizer.py",
    f"src/{package_name}/cleaner.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb",
    "examples/demo.ipynb",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file
        print(f"Creating empty file: {filepath}")
    else:
        print(f"File already exists: {filepath}")