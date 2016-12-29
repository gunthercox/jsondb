#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HISTORY = open('history.rst').read().replace('.. :changelog:', '')

README = lambda f: open(f, 'r').read()

# Dynamically import the package information
JSONDB = __import__('jsondb')
VERSION = JSONDB.__version__
AUTHOR = JSONDB.__author__
AUTHOR_EMAIL = JSONDB.__email__
URL = JSONDB.__url__
DESCRIPTION = JSONDB.__doc__

setup(
    name='jsondatabase',
    version=VERSION,
    description=DESCRIPTION,
    long_description=README('readme.md') + '\n\n' + HISTORY,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=['pymongo'],
    packages=['jsondb'],
    package_dir={'jsondb': 'jsondb'},
    include_package_data=True,
    license='BSD',
    zip_safe=True,
    keywords=['jsondb'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=[]
)
