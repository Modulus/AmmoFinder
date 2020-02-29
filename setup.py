#!/usr/bin/env python3.7
# Non-standard library python package imports
from setuptools import (  # type: ignore
    find_packages,
    setup,
)

# Internal module package imports
from ammo_finder import version

setup(
    name="ammo_finder",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "beautifulsoup4==4.8.2",
        "bs4==0.0.1",
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "idna==2.9",
        "requests==2.23.0",
        "soupsieve==2.0",
        "urllib3==1.25.8",
    ],
    entry_points="""
        [console_scripts]
        ammo_finder=ammo_finder.cli:main
    """,
)
