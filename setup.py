#!/usr/bin/env python
# This file is managed by `git_helper`. Don't edit it directly
"""Setup script"""


from setuptools import setup, find_packages

setup(
		author="Dominic Davis-Foster",
		name="demos",
		packages=find_packages(exclude=("tests", "doc-source")),
		version="1",
		)
