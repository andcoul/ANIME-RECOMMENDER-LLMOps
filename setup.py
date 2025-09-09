from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="amine_recommender",
    version="0.1",
    author="Andy",
    packages=find_packages(),
    install_requires=requirements,
)