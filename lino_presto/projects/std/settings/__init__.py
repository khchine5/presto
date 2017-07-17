# -*- coding: UTF-8 -*-
# Copyright 2011-2017 Luc Saffre
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

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino Presto"
    version = "0.1"
    url = "http://presto.lino-framework.org"

    demo_fixtures = 'std demo minimal_ledger euvatrates demo_bookings payments demo2'.split()

    languages = 'en de fr et'

    project_model = 'tickets.Project'
    workflows_module = 'lino_presto.lib.presto.workflows'

    user_types_module = 'lino_presto.lib.presto.user_types'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.users'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_presto.lib.contacts'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.lists'
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
        yield 'lino_xl.lib.stars'
        yield 'lino_xl.lib.meetings'
        yield 'lino_presto.lib.tickets'
        yield 'lino_xl.lib.faculties'
        yield 'lino_xl.lib.votes'
        # yield 'lino_presto.lib.clocking'
        yield 'lino_xl.lib.clocking'
        yield 'lino_xl.lib.deploy'
        yield 'lino.modlib.uploads'
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

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')
        # self.plugins.comments.configure(
        #     commentable_model='tickets.Ticket')

    def unused_get_dashboard_items(self, user):
        if False:
            from lino.utils.weekly import get_report

            def datefmt(d):
                T = self.modules.clocking.MySessionsByDate
                sar = T.request_from(
                    ar, param_values=dict(start_date=d, end_date=d))
                return ar.href_to_request(
                    sar, str(d.day), style="font-size:xx-small;")

            yield get_report(ar, datefmt=datefmt)
        # yield self.modules.clocking.WorkedHours
        # yield self.modules.tickets.MyTickets
        # yield self.modules.tickets.ActiveTickets

