#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="demo_calculcan",
    version="0.0.1",
    description="Demo for calcul canada usage with and without hydra/submitit",
    author="",
    author_email="",
    url="https://github.com/arnaudjudge/demo_calculcan",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    # entry_points={
    #     "console_scripts": [
    #         "train_command = src.train:main",
    #     ]
    # },
)