# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
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
"""Choicelists for :mod:`lino_presto.lib.clocking`.

"""

from __future__ import unicode_literals

from django.db import models
from lino.api import dd, _


class PaymentModes(dd.ChoiceList):
    verbose_name = _("Payment mode")
    verbose_name_plural = _("Payment modes")

add = PaymentModes.add_item

add('10', _("Free"), 'free')
add('20', _("Cash"), 'cash')
add('30', _("Invoice"), 'invoice')
add('40', _("Later"), 'later')


class SessionStates(dd.Workflow):
    required_roles = dd.login_required(dd.SiteAdmin)
    invoiceable = models.BooleanField(_("invoiceable"), default=True)

add = SessionStates.add_item
add('10', _("Draft"), 'draft', editable=True, invoiceable=False)
add('20', _("Closed"), 'closed', editable=False, invoiceable=False)
add('30', _("Cancelled"), 'cancelled', editable=False, invoiceable=False)
add('40', _("Missed"), 'missed', editable=False, invoiceable=True)

