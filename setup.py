# -*- coding: utf-8 -*-

# Learn more: https://github.com/senseibara/sandwich

import pathlib
from setuptools import setup, find_packages


readme = pathlib.Path('README.md').read_text()
license = pathlib.Path('LICENSE').read_text()

setup(
    name='sandwich',
    version='0.1.0',
    description='sandwich package',
    long_description=readme,
    author='Senseibara',
    author_email='ndiayebara93@gmail.com',
    url='https://github.com/senseibara/sandwich',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

