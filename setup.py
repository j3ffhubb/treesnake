#!/usr/bin/env python
"""
This file is part of the treesnake project, Copyright Jeff Hubbard

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
"""

import setuptools
import os
import sys

setuptools.setup(
    name="treesnake",
    version="1.0",
    author="Jeff Hubbard",
    author_email='musikernel@nospam.org',
    license='GPL 3.0',
    description='Tree-family data structures',
    url='https://github.com/j3ffhubb/treesnake',
    packages=setuptools.find_packages(),
    include_package_data=True,
)

