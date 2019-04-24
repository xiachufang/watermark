# coding: utf-8

import io

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xiachufang-watermark',

    version='0.0.7',

    description='xcf watermark tools',
    long_description=long_description,

    url='https://github.com/xiachufang/watermark',

    # Author details
    author='garland',
    author_email='garland@xiachufang.com',
    packages=find_packages(exclude=['docs', 'tests*']),

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['pillow'],
    include_package_data=True
)
