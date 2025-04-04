from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="archivertools",
    version="1.0.0",
    author="Andrea Pollastro",
    author_email="apollastro@lbl.gov",
    description="A Python package for interacting with EPICS archiver data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrea-pollastro/archivertools",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.10",
    keywords="epics, archiver, data, science, research",
)