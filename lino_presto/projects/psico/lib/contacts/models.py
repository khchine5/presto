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
"""Database models for this plugin."""

from __future__ import unicode_literals

from lino.api import _

from lino_presto.lib.contacts.models import *

from .choicelists import PartnerTariffs
from lino_xl.lib.clocking.mixins import Workable


class Partner(Partner, Workable):

    class Meta(Partner.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Partner')

    obsoletes = dd.ForeignKey(
        'self', blank=True, null=True, related_name='obsoleted_by')

    tariff = PartnerTariffs.field(
        default=PartnerTariffs.plain.as_callable())


class Person(Partner, Person):

    class Meta(Person.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Person')


class Company(Partner, Company):

    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')


dd.update_field(Person, 'first_name', blank=True)
