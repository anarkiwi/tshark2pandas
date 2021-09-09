#!/usr/bin/env python

import setuptools
import subprocess

# TODO: not currently possible to call make with pbr (https://bugs.launchpad.net/pbr/+bug/1737664)
setuptools.setup(
    name='tshark2pandas',
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    python_requires='>=3.8',
    pbr=True,
    packages=['tshark2pandas'],
    package_data={'': ['tshark2pandas_jsonfilter']},
)
