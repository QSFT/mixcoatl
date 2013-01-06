#!/usr/bin/env python

import mixcoatl

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'mixcoatl',
    'mixcoatl.admin',
    'mixcoatl.config',
    'mixcoatl.decorators',
    'mixcoatl.exceptions',
    'mixcoatl.geography',
    'mixcoatl.infrastructure',
    'mixcoatl.network',
    'mixcoatl.settings'
]

setup(
    name='mixcoatl',
    version=mixcoatl.__version__,
    description='enStratus API Python wrapper',
    long_description=open('README.md').read(),
    author='John E. Vincent',
    author_email='lusis.org+github.com@gmail.com',
    url='https://github.com/enStratus/mixcoatl',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'mixcoatl': 'mixcoatl'},
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    license=open('LICENSE').read(),
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
