#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

history = open("history.rst").read().replace(".. :changelog:", "")

readme = lambda f: open(f, "r").read()

setup(
    name="jsondatabase",
    version="0.0.5",
    description="A flat file database for json objects.",
    long_description=readme("readme.md") + "\n\n" + history,
    author="Gunther Cox",
    author_email="gunthercx@gmail.com",
    url="https://github.com/gunthercox/jsondb",
    packages=["jsondb"],
    package_dir={"jsondb": "jsondb"},
    include_package_data=True,
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords = ["jsondb"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    test_suite="tests",
    tests_require=[]
)
