#!/usr/bin/env python

from distutils.core import setup

setup(name='privatebeta',
      version='0.4.1',
      description='A reusable application for collecting email addresses for later invitations and to restrict access to a site under private beta.',
      author='Pragmatic Badger, LLC.',
      author_email='info@pragmaticbadger.com',
      url='http://github.com/pragmaticbadger/django-privatebeta/',
      packages=['privatebeta', 'privatebeta.migrations'],
      package_dir={'privatebeta': 'privatebeta'},
     )