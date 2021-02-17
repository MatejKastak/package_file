import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name="package_file",
    version="0.0.1",
    author="Matej Kastak",
    author_email="matej.kastak@gmail.com",
    description="No description",
    long_description="asd",
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=find_packages(),
    entry_points={"console_scripts": ["package_file = src.main:main"]},
    # This should include MANIFEST.in
    include_package_data=True,
    # This will include './src/data/*.json'
    package_data={
        'src': ['data/*.json'],
    }
)
