import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="earcut",
    version="1.1.5",
    description="A pure Python port of the earcut JS triangulation library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vojtatom/earcut-python",
    author="Metacity",
    license="ISC",
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["earcut"],
    python_requires='>=3.8',                # Minimum version requirement of the package
    install_requires=["numpy"]              # Install other dependencies if any
)

