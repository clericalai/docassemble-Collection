#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.Collection',
      version='0.8',
      description=('Validation and do not call letters to send to debt collectors.'),
      long_description='# docassemble-madebtcollections\r\n\r\n## Changelog\r\n\r\n* 2018-09-26 Stripped down validation/exemption/do-not call letter to more basic \r\n  functionality. Removed statements about social security income.\r\n  \r\n* 2018-09-26 removed GBLS logo from validationOnly template.\r\n\r\n* 2018-09-26 fixed bug where interview used wrong template.\r\n\r\n* 2018-09-26 fixed additional bug where interview used wrong template.\r\n\r\n* 2018-10-04 added metadata block to display interview title on GBLS website.\r\n\r\n* 2018-10-09 added signature capability to validationOnly interview.\r\n\r\n* 2018-10-15 corrected bug where validationOnly template included do not call language\r\n  in validation letters.\r\n  \r\n* 2018-10-15 added client address to address block in template.',
      long_description_content_type='text/markdown',
      author='Matt Brooks',
      author_email='Mbrooks@gbls.org',
      license='MIT',
      url='https://www.gbls.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/Collection/', package='docassemble.Collection'),
     )

