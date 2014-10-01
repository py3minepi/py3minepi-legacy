#!/usr/bin/env python
import io
from setuptools import setup, find_packages
import sys

with io.open('README.rst', mode='r', encoding='utf8') as f:
    readme = f.read()


dependencies = []
if sys.version_info[:2] < (3, 4):
    dependencies.append('enum34')


setup(name='py3minepi',
      version='0.0.1',
      description='A better minecraft pi library.',
      url='https://github.com/py3minepi/py3minepi',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      zip_safe=True,
      include_package_data=True,
      keywords='minecraft raspberry pi mcpi py3minepi',
      long_description=readme,
      install_requires=dependencies,
      classifiers=[
          'Development Status :: Development Status :: 3 - Alpha',
          'Environment :: X11 Applications',
          'Intended Audience :: Education',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Other/Proprietary License',  # TODO fix
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
)
