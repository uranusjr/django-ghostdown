#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from importlib import import_module
from setuptools import setup


os.chdir(os.path.dirname(os.path.abspath(__file__)))


long_description = open('README.rst').read()
version = import_module('ghostdown').__version__

# Find packages to install.
packages = []
for dirpath, dirnames, filenames in os.walk('ghostdown'):
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split('/')).encode('utf-8'))

# Load requirements from requirement file.
with open('requirements/project.txt') as f:
    install_requires = [p for p in f.readlines() if p]


setup(
    name='django-ghostdown',
    url='https://github.com/uranusjr/django-ghostdown',
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    description='Ghost-like markdown editor as a Django form widget.',
    long_description=long_description,
    version=version,
    install_requires=install_requires,
    license='MIT License',
    packages=packages,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
