#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='xivo_auth-example-backend',
    version='0.0.1',

    description='A simple example backend plugin for xivo-auth',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'wazo_auth.backends': [
            'example = example_backend.example:ExampleBackend',
        ],
    }
)
