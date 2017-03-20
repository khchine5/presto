# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
#
# This file is part of Lino Presto.
#
# Lino Presto is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Presto is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Presto.  If not, see
# <http://www.gnu.org/licenses/>.

"""
The settings package.

.. autosummary::
   :toctree:

   demo
   doctests
   memory



"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino for psychologists"

    version = "0.1"
    url = "http://presto.lino-framework.org/psico"
    
    demo_fixtures = 'std demo novat minimal_ledger demo_bookings payments demo2'.split()
    project_model = 'contacts.Partner'

    languages = 'en de fr et'
    
    # workflows_module = 'lino_xl.lib.tickets.workflows'

    user_types_module = 'lino_presto.lib.presto.user_types'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.users'
        yield 'lino_presto.projects.psico.lib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_presto.projects.psico.lib.contacts'
        yield 'lino_xl.lib.households'
        yield 'lino_presto.projects.psico.lib.lists'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.humanlinks',
        # yield 'lino_xl.lib.products'
        # yield 'lino_noi.lib.products'
        # yield 'lino_xl.lib.accounts'
        yield 'lino_xl.lib.sales'
        # yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.invoicing'
        # 'lino_xl.lib.projects',
        yield 'lino_xl.lib.blogs'
        yield 'lino_xl.lib.notes'
        # yield 'lino_presto.lib.tickets'
        yield 'lino_xl.lib.faculties'
        # yield 'lino_xl.lib.votes'
        yield 'lino_presto.projects.psico.lib.clocking'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_presto.lib.clocking'
        # yield 'lino.modlib.uploads'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.cal'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.appypod'
        # yield 'lino_xl.lib.postings'
        # yield 'lino_xl.lib.pages'

        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.plausibility'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'

        yield 'lino_presto.lib.presto'
        yield 'lino_presto.projects.psico.lib.teams'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')
        self.plugins.clocking.configure(ticket_model='contacts.Partner')
        self.plugins.faculties.configure(demander_model='contacts.Partner')

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
