# Copyright 2015, Luc Saffre
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

from lino.api import dd


@dd.receiver(dd.post_analyze)
def my_details(sender, **kw):
    site = sender
    site.modules.accounts.Accounts.set_detail_layout("""
    ref:10 name id:5
    seqno group type clearable
    ledger.MovementsByAccount
    """)

    site.modules.system.SiteConfigs.set_detail_layout("""
    site_company next_partner_id:10
    default_build_method
    clients_account   sales_account
    suppliers_account purchases_account tax_offices_account
    wages_account clearings_account
    max_auto_events default_event_type site_calendar
    """)
