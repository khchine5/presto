# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# This file is part of Lino Presto.
# Lino Presto is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# Lino Presto is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public
# License along with Lino Presto.  If not, see
# <http://www.gnu.org/licenses/>.

# Note that this module may not have a docstring because any
# global variable defined here will override the global
# namespace of lino/__init__.py who includes it with execfile.

# This module is part of the Lino test suite.
# To test just this module:
#
#   $ python setup.py test -s tests.PackagesTests

from __future__ import unicode_literals

SETUP_INFO = dict(
    name='lino_presto',
    version='0.0.1',
    install_requires=['lino_cosi', 'lino_noi'],
    tests_require=[],

    description="A Lino application which combines Cosi and Noi",
    license='GNU Affero General Public License v3',
    include_package_data=True,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://presto.lino-framework.org",
    #~ test_suite = 'lino.test_apps',
    test_suite='tests',
    classifiers="""\
  Programming Language :: Python
  Programming Language :: Python :: 2
  Development Status :: 4 - Beta
  Environment :: Web Environment
  Framework :: Django
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: GNU Affero General Public License
  Natural Language :: English
  Natural Language :: French
  Natural Language :: German
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business""".splitlines())

SETUP_INFO.update(long_description="""\

Lino Presto is an application for managing the work of organisations
where time is money, i.e. where time tracker sessions are the base for
writing invoices.

- For *introductions* and *commercial information* about Lino Presto
  please see `www.saffre-rumma.net
  <http://www.saffre-rumma.net/presto/>`__.

- The central project homepage is http://presto.lino-framework.org

The name "Presto" originally comes from "prestations de service", the
French expression for service providements.  It also means "quick" in
Italian.

**Status: not yet usable**

It is a seamless combination of the following general functionalities:

- Accounting (general ledger, sales, purchases, VAT declarations, bank
  journals, ...)

- Project management, issue tracking, generating service reports and
  invoices for services.

Maybe later:

- Subscription management (generating regular invoices based to
  subscription contracts)

- Content management, blogs, newsletters and classical web pages

Lino-Presto is not yet usable.  When one day it will be ready, we plan
it to be reusable by other service providers such as software
developers, tax consultants, accountants,...

""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_presto
lino_presto.lib
lino_presto.lib.contacts
lino_presto.lib.contacts.fixtures
lino_presto.lib.presto
lino_presto.lib.presto.fixtures
lino_presto.lib.tickets
lino_presto.projects
lino_presto.projects.std
lino_presto.projects.std.settings
lino_presto.projects.psico
lino_presto.projects.psico.tests
lino_presto.projects.psico.settings
lino_presto.projects.psico.lib
lino_presto.projects.psico.lib.clocking
lino_presto.projects.psico.lib.clocking.fixtures
lino_presto.projects.psico.lib.contacts
lino_presto.projects.psico.lib.contacts.fixtures
lino_presto.projects.psico.lib.lists
lino_presto.projects.psico.lib.lists.fixtures
lino_presto.projects.psico.lib.teams
lino_presto.projects.psico.lib.teams.fixtures
lino_presto.projects.psico.lib.users
lino_presto.projects.psico.lib.users.fixtures
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino': [
        ('**/sandbox/**',        'ignore', None),
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**/linoweb.js',        'jinja2', None),
        #~ ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
        #~ ('**/templates/**.txt',  'genshi', {
        #~ 'template_class': 'genshi.template:TextTemplate'
        #~ })
    ],
})

SETUP_INFO.update(package_data=dict())
