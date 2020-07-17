#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
		author="Dominic Davis-Foster",
		name="demos",
		packages=find_packages(exclude=("tests", "doc-source")),
		version="1",
		)
