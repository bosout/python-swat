#!/usr/bin/env python

''' Install the SWAT module '''

from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import struct
import sys


class SWATInstaller(install):
    ''' Make sure that the Python executable is 64-bit '''
    def run(self):
        size = struct.calcsize('P')  # integer size
        if size != 8:
            print('Sorry, you must have 64bit Python installed.')
            print('Exiting.')
            print('This version of Python is %dbit:' % (size*8))
            print(sys.version)
            raise Exception('requires 64bit')
        install.run(self)

#
# The resulting directory structure will look like:
#
#    lib/(SWAT precompiled libraries)
#        python#.#/
#            site-packages/
#                swat/
#                    __init__.py
#                    others.py
#

setup(
    cmdclass = {'install': SWATInstaller},
    zip_safe = False,
    name = 'swat',
    version = '0.9.0',
    description = 'SAS Wrapper for Analytics Transfer (SWAT)',
    long_description = open('README.rst').read(),
    author = 'Kevin D Smith',
    author_email = 'Kevin.Smith@sas.com',
    url = 'http://github.com/sassoftware/python-swat/',
    license = 'LICENSE.txt',
    packages = find_packages(),
    package_data = {
        'swat': ['lib/*/*.so', 'lib/*/*.pyd*', 'lib/*/*.dll'],
    },
    install_requires = [
        "pandas >= 0.16.0",
        "six >= 0.9.0",
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)