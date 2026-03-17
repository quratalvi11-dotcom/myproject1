from setuptools import setup, find_packages

setup(
    name="dataquick",
    version="0.1.1",
    author="quratalvi11-dotcom",
    description="A fast and easy Auto EDA library for data scientists",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/quratalvi11-dotcom/myproject1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
    ],
)
