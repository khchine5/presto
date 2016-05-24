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
"""Choicelists for this plugin.

"""

from lino.api import dd, _


class PartnerTariffs(dd.ChoiceList):
    verbose_name = _("Partner tariff")
    verbose_name_plural = _("Partner tariffs")

add = PartnerTariffs.add_item

add('10', _("Plain"), 'plain')
add('20', _("Reduced"), 'reduced')


