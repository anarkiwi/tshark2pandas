#!/usr/bin/env python

import setuptools
import subprocess

setuptools.setup(
    name='tshark2pandas',
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    python_requires='>=3.8',
    pbr=True,
    packages=['tshark2pandas'],
    package_data={'': ['tshark2pandas_jsonfilter']},
)
