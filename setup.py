#!/usr/bin/env python3.7

# Python standard library imports
from pathlib import Path

# Non-standard library python package imports
from setuptools import (  # type: ignore
    find_packages,
    setup,
)

# Internal module package imports
from ammo_finder import version


readme_md_file = Path(__file__).parent / 'README.md'

setup(
    name='ammo_finder',
    version=version,
    author='https://github.com/Modulus',
    description='Python webscraping tool for finding prices for ammunition in Norway.',
    long_description=readme_md_file.read_text() if readme_md_file.is_file() else '',
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    python_requires='~=3.7',
    install_requires=[
        "beautifulsoup4==4.8.2",
        "bs4==0.0.1",
        "certifi==2022.12.7",
        "chardet==3.0.4",
        "idna==2.9",
        "requests==2.23.0",
        "soupsieve==2.0",
        "urllib3==1.25.8",
    ],
    entry_points="""
    """,
)
