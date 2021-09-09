#!/usr/bin/env python

import setuptools
import subprocess
from distutils.command.build_py import build_py


class BuildCommand(build_py):

    def run(self):
        command = ['make', '--directory=tshark2pandas']
        subprocess.check_call(command)
        super().run()


setuptools.setup(
    name='tshark2pandas',
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    python_requires='>=3.8',
    packages=['tshark2pandas'],
    package_data={'': ['tshark2pandas_jsonfilter']},
    cmdclass={'build_py': BuildCommand},
)
