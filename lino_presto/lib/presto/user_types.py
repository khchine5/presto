# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
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


"""Defines a default set of user roles and fills
:class:`lino.modlib.users.choicelists.UserTypes`.

This is used as the :attr:`user_types_module
<lino.core.site.Site.user_types_module>` for
:mod:`lino_presto.projects.std`.


"""

from lino.api import _
from lino.modlib.users.choicelists import UserTypes
from lino.core.roles import UserRole, SiteAdmin
from lino_xl.lib.contacts.roles import ContactsUser
from lino_xl.lib.products.roles import ProductsUser, ProductsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino.modlib.office.roles import OfficeStaff, OfficeUser
from lino_xl.lib.ledger.roles import LedgerUser, LedgerStaff
from lino_xl.lib.sepa.roles import SepaUser, SepaStaff
from lino_xl.lib.tickets.roles import Triager
from lino_xl.lib.clocking.roles import Worker


class Secretary(ContactsUser, OfficeUser, LedgerUser, SepaUser,
                ExcerptsUser, ProductsStaff):
    pass


class Consultant(ContactsUser, OfficeUser, LedgerUser, SepaUser,
                 Worker, ExcerptsUser, ProductsUser):
    pass


class SiteAdmin(SiteAdmin, OfficeStaff, LedgerStaff, SepaStaff,
                Worker, Triager, ExcerptsStaff, ProductsStaff):
    pass

UserTypes.clear()

add = UserTypes.add_item

add('000', _("Anonymous"), UserRole, name='anonymous', readonly=True)
add('100', _("Secretary"), Secretary)
add('200', _("Consultant"), Consultant)
add('900', _("Administrator"), SiteAdmin, name='admin')

