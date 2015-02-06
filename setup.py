#!/usr/bin/env python

import mixcoatl
import os
import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'mixcoatl',
    'mixcoatl.admin',
    'mixcoatl.analytics',
    'mixcoatl.automation',
    'mixcoatl.config',
    'mixcoatl.decorators',
    'mixcoatl.exceptions',
    'mixcoatl.geography',
    'mixcoatl.infrastructure',
    'mixcoatl.network',
    'mixcoatl.platform',
    'mixcoatl.settings'
]

requires = ['requests==1.0.4', 'prettytable==0.7.2', 'dicttoxml==1.5.8', 'termcolor==1.1.0']
setup(
    name='mixcoatl',
    version=mixcoatl.__version__,
    description='Dell Cloud Manager API Python wrapper',
    long_description='Dell Cloud Manager API Python wrapper',
    author='Dell Cloud Management Team',
    author_email='mixcoatl@enstratius.com',
    url='https://github.com/enStratus/mixcoatl',
    packages=packages,
    package_data={'': ['LICENSE', 'README.rst', 'requirements.txt']},
    package_dir={'mixcoatl': 'mixcoatl'},
    include_package_data=True,
    install_requires=requires,
    scripts=glob.glob(os.path.join('bin','*')),
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
