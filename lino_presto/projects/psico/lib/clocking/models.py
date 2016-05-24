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

from __future__ import unicode_literals

from lino.api import _

from lino_noi.lib.clocking.models import *

from lino_cosi.lib.invoicing.mixins import Invoiceable

from .choicelists import PaymentModes, SessionStates


class Session(Session, Invoiceable):

    class Meta(Session.Meta):
        app_label = 'clocking'
        abstract = dd.is_abstract_model(__name__, 'Session')

    invoiceable_date_field = 'end_date'

    fee = dd.ForeignKey('products.Product',
                        blank=True, null=True,
                        related_name='sessions_by_fee')

    amount_received = dd.PriceField(
        _("Amount received"), blank=True, null=True)

    payment_mode = PaymentModes.field(blank=True)
    state = SessionStates.field(
        default=SessionStates.draft.as_callable())

    @classmethod
    def get_invoiceables_for_plan(cls, plan, partner=None):

        qs = cls.objects.filter(**{
            cls.invoiceable_date_field + '__lte': plan.max_date})
        if partner is None:
            partner = plan.partner
        if partner:
            q1 = models.Q(
                partner__invoice_recipient__isnull=True,
                partner=partner)
            q2 = models.Q(partner__invoice_recipient=partner)
            qs = cls.objects.filter(models.Q(q1 | q2))
        else:
            return []
        # dd.logger.info("20160513 %s (%d rows)", qs.query, qs.count())
        return qs.order_by(cls.invoiceable_date_field)

    def get_invoiceable_amount(self):
        return 123  # TODO: tarification rules

    def get_invoiceable_qty(self):
        return 1

    def setup_invoice_item(self, item):
        item.description = dd.plugins.jinja.render_from_request(
            None, 'clocking/Session/item_description.html',
            obj=self, item=item)

    def get_invoiceable_product(self):
        # dd.logger.info('20160223 %s', self.course)
        if not self.state.invoiceable:
            return
        return self.fee


Sessions.detail_layout = """
ticket:40 user:20 faculty:20
start_date start_time end_date end_time break_time duration
summary:60 workflow_buttons:20
fee payment_mode amount_received state
description
"""
Sessions.insert_layout = """
ticket
summary
session_type
"""
