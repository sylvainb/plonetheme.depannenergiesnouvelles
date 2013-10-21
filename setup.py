#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0dev'

tests_require = ['zope.testing',
                 'zope.app.testing',
                 'plone.app.testing',
                 'lxml']

setup(name='plonetheme.depannenergiesnouvelles',
      version=version,
      description="Plone Theme for www.depann-energies-nouvelles.fr website",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone web zope python theme diazo plone.app.theming',
      author='Sylvain Boureliou [sylvainb]',
      author_email='sylvain.boureliou@gmail.com',
      url='http://www.boureliou.com',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.jbot',
          # -*- Extra requirements: -*-
          'five.grok',
          'Products.PloneFormGen==1.7.12',
          'webcouturier.dropdownmenu==2.3.1',
          'collective.quickupload==1.6.0',
          'collective.googleanalytics==1.4.3'
      ],
      tests_require=tests_require,
      extras_require={
          'test': tests_require,
      },
      test_suite='plonetheme.depannenergiesnouvelles.tests.test_docs.test_suite',
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
