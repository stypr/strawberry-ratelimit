#!/usr/bin/python -u
#-*- coding: utf-8 -*-
"""
    setup.py
    For pypi
"""
from setuptools import setup

def _requires_from_file(filename):
    return open(filename).read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="strawberry-ratelimit",
    packages=["strawberry_ratelimit"],
    version="1.0",
    license="MIT",
    description=("Strawberry GraphQL Ratelimit Extension"),
    author="Harold Kim",
    author_email="root@stypr.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stypr/strawberry-ratelimit",
    download_url="https://github.com/stypr/strawberry-ratelimit/archive/v1.0.tar.gz",
    keywords=[
        "strawberry-graphql",
        "strawberry",
        "extension",
        "ratelimit",
    ],
    install_requires=_requires_from_file("requirements.txt"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
