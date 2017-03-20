# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Luc Saffre
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

from lino.api import dd, rt, _

from lino_cosi.lib.contacts.models import *

from lino_xl.lib.cal.workflows import feedback
from lino_xl.lib.addresses.mixins import AddressOwner


class Partner(Partner, AddressOwner, mixins.CreatedModified):

    class Meta(Partner.Meta):
        app_label = 'contacts'
        # verbose_name = _("Partner")
        # verbose_name_plural = _("Partners")
        abstract = dd.is_abstract_model(__name__, 'Partner')

    isikukood = models.CharField(
        _("isikukood"), max_length=20, blank=True)

    hidden_columns = 'created modified'

    faculty = None
    """Required by :mod:`lino_xl.lib.clocking`.
    """

    def get_overview_elems(self, ar):
        # In the base classes, Partner must come first because
        # otherwise Django won't inherit `meta.verbose_name`. OTOH we
        # want to get the `get_overview_elems` from AddressOwner, not
        # from Partner (i.e. AddressLocation).
        elems = super(Partner, self).get_overview_elems(ar)
        elems += AddressOwner.get_overview_elems(self, ar)
        return elems


class PartnerDetail(PartnerDetail):

    main = "general contact #tickets ledger misc "

    general = dd.Panel("""
    overview:20 general2:20 general3:40
    # notes.NotesByPartner
    """, label=_("General"))

    general2 = """
    id language
    url
    """

    # tickets = "tickets.SponsorshipsByPartner"

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    address_box
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    ledger = dd.Panel("""
    vat.VouchersByPartner
    ledger.MovementsByPartner
    """, label=dd.plugins.ledger.verbose_name)

    misc = dd.Panel("""
    created modified
    """, label=_("Miscellaneous"))


class Person(Partner, Person):
    """
    Represents a physical person.
    """

    class Meta(Person.Meta):
        app_label = 'contacts'
        # verbose_name = _("Person")
        # verbose_name_plural = _("Persons")
        #~ ordering = ['last_name','first_name']
        abstract = dd.is_abstract_model(__name__, 'Person')

    def get_queryset(self, ar):
        return self.model.objects.select_related('country', 'city')

    def get_print_language(self):
        "Used by DirectPrintAction"
        return self.language

dd.update_field(Person, 'first_name', blank=False)
dd.update_field(Person, 'last_name', blank=False)


class PersonDetail(PersonDetail):

    main = "general contact #tickets misc"

    general = dd.Panel("""
    overview:20 general2:40 general3:40
    contacts.RolesByPerson:20 households.MembersByPerson:40 \
    humanlinks.LinksByHuman
    """, label=_("General"))

    general2 = """
    title first_name:15 middle_name:15
    last_name
    gender:10 birth_date age:10
    id language
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    lists.MembersByPartner
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    # tickets = "tickets.SponsorshipsByPartner"

    misc = dd.Panel("""
    url
    created modified
    # notes.NotesByPartner
    """, label=_("Miscellaneous"))


class Persons(Persons):

    detail_layout = PersonDetail()


class Company(Partner, Company):
    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')

    # class Meta:
    #     verbose_name = _("Organisation")
    #     verbose_name_plural = _("Organisations")

    # vat_id = models.CharField(_("VAT id"), max_length=200, blank=True)


class CompanyDetail(CompanyDetail):

    main = "general contact #tickets misc"

    general = dd.Panel("""
    overview:20 general2:40 general3:40
    contacts.RolesByCompany
    """, label=_("General"))

    general2 = """
    prefix:20 name:40
    type vat_id
    url
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    lists.MembersByPartner
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    # tickets = "tickets.SponsorshipsByPartner"

    misc = dd.Panel("""
    id language
    created modified
    # notes.NotesByPartner
    """, label=_("Miscellaneous"))


class Companies(Companies):
    detail_layout = CompanyDetail()


Partners.set_detail_layout(PartnerDetail())
Companies.set_detail_layout(CompanyDetail())

# @dd.receiver(dd.post_analyze)
# def my_details(sender, **kw):
#     contacts = sender.modules.contacts

#     contacts.Partners.set_detail_layout(contacts.PartnerDetail())
#     contacts.Companies.set_detail_layout(contacts.CompanyDetail())


