from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="archivertools", # Replace with your username
    version="1.0.0",
    author="Andrea Pollastro",
    author_email="apollastro@lbl.gov",
    description="archivertools is a module to interact with the archiver server through Python.",
    url="https://git.als.lbl.gov/physics/researchdev/archivertools",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)