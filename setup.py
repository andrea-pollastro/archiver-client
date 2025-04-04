from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="archivertools",
    version="1.0.0",
    author="Andrea Pollastro",
    author_email="apollastro@lbl.gov",
    packages=find_packages(),
    install_requires=requirements,
    description="A Python package for interacting with EPICS archiver data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andrea-pollastro/archivertools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)