# coding: utf-8

"""
unicorn is a french and a 'what the fuck' wrapper around the git CLI

inspired by brouberol/marcel <https://github.com/brouberol/marcel/blob/master/setup.py>
"""


import re

from os.path import dirname, join, abspath
from setuptools import setup, find_packages()

VERSION = re.search(
    r"__version__\s=\s'(\d\.\d\.\d)'",
    open(abspath(join(dirname(__file__), 'unicorn.py'))).read()
    ).group(1)

setup(
    name="unicorn",
    version=VERSION,
    license='3-clause BSD',
    description='Le git français et WTF',
    author="Thiebaudet Thomas, Grévin Nicolas, Jean-Philippe Maligne",
    author_email="thomas@thiebaudet.fr, developer@nicolas-grevin.com, jpmaligne@gmail.com",
    url='https://github.com/Unicorn-stomperZ/git-alphabet',
    py_modules=['marcel'],
    entry_points={'console_scripts': ['unicorn=unicorn:main']},
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        ],
    packages=find_packages()
)
