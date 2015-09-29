# Copyright 2011-2015 Luc Saffre
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino Presto"
    version = "0.1"
    url = "http://presto.lino-framework.org"

    demo_fixtures = 'std few_languages props democfg demo demo2'.split()

    languages = 'en de fr et'

    project_model = 'tickets.Project'

    user_profiles_module = 'lino_noi.lib.noi.roles'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino.modlib.users'
        yield 'lino.modlib.countries'
        yield 'lino.modlib.properties'
        yield 'lino_presto.lib.contacts'
        yield 'lino.modlib.households'
        yield 'lino.modlib.lists'
        yield 'lino.modlib.addresses'
        yield 'lino.modlib.humanlinks',
        yield 'lino.modlib.products'
        yield 'lino_cosi.lib.accounts'
        # yield 'lino.modlib.ledger'
        yield 'lino_cosi.lib.vat'
        yield 'lino_cosi.lib.sepa'
        yield 'lino_cosi.lib.finan'
        yield 'lino_cosi.lib.auto.sales'
        #~ 'lino.modlib.projects',
        yield 'lino.modlib.blogs'
        yield 'lino.modlib.notes'
        yield 'lino_noi.lib.clocking'
        # yield 'lino.modlib.uploads'
        yield 'lino.modlib.extensible'
        yield 'lino.modlib.cal'
        # yield 'lino.modlib.outbox'
        # yield 'lino.modlib.excerpts'
        #~ yield 'lino.modlib.postings'
        #~ yield 'lino.modlib.pages'

        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.plausibility'
        yield 'lino.modlib.tinymce'

        yield 'lino_presto.lib.presto'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')

    def get_admin_main_items(self, ar):
        if False:
            from lino.utils.weekly import get_report

            def datefmt(d):
                T = self.modules.clocking.MySessionsByDate
                sar = T.request_from(
                    ar, param_values=dict(start_date=d, end_date=d))
                return ar.href_to_request(
                    sar, str(d.day), style="font-size:xx-small;")

            yield get_report(ar, datefmt=datefmt)
        yield self.modules.clocking.WorkedHours
        # yield self.modules.tickets.MyTickets
        yield self.modules.tickets.ActiveTickets

