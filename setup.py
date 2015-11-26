#!/usr/bin/env python
"""
Install wagtailtestutils using setuptools
"""
from setuptools import setup, find_packages

with open('wagtailtestutils/version.py', 'r') as f:
    version = None
    exec(f.read())

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='wagtailtestutils',
    version=version,
    description='Test utils for Wagtail sites',
    long_description=readme,
    author='Tim Heap',
    author_email='tim@takeflight.com.au',
    url='https://bitbucket.org/takeflight/wagtailtestutils',

    install_requires=['wagtail>=1.2'],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
