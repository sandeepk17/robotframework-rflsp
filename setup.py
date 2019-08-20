# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
from setuptools import setup, find_packages

CWD = abspath(dirname(__file__))
PACKAGE_NAME='rflsp'
with open(join(CWD, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION="0.0.1"

with open(join(CWD, 'requirements.txt'), encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

CLASSIFIERS='''
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Topic :: Software Development :: Libraries
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
Topic :: Utilities
Operating System :: MacOS
Operating System :: Microsoft :: Windows
Operating System :: POSIX :: Linux
Operating System :: POSIX :: Other
'''.strip().splitlines()

setup(name="{}".format(PACKAGE_NAME),
      version=VERSION,
      description='Language Server Protocol implementation for Robot Framework',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=CLASSIFIERS,
      url='https://github.com/rasjani/robotframework-{}'.format(PACKAGE_NAME),
      author='Jani Mikkonen',
      author_email='jani.mikkonen@gmail.com',
      license='APACHE',
      packages=[PACKAGE_NAME],
      package_dir={PACKAGE_NAME: 'src/{}'.format(PACKAGE_NAME)},
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False)
