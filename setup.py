#!/usr/bin/env python
from setuptools import setup

setup(
    name='tshark2pandas',
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    python_requires='>=3.8',
    packages=['tshark2pandas'],
    pbr=True,
    package_data={"": ["tshark2pandas_jsonfilter"]},
)
