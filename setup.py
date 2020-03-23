from os import path
from setuptools import setup, find_packages

DEPENDENCIES = ["flask", "pytube3", "forked-auditok-split-without-data"]
TEST_DEPENDENCIES = ["pylint", "pytest", "pytest-mock"]


def get_long_description():
    workspace = path.abspath(path.dirname(__file__))
    with open(path.join(workspace, "README.md"), encoding="utf-8") as readme:
        return readme.read()


setup(
    name="auditok-server",
    version="0.1.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    install_requires=DEPENDENCIES,
    test_require=TEST_DEPENDENCIES,
    extras_require={"test": TEST_DEPENDENCIES},
)
