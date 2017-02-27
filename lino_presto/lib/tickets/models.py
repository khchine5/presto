# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

from lino_noi.lib.tickets.models import *
from lino.api import _

dd.update_field(
    'tickets.Ticket', 'upgrade_notes', verbose_name=_("Solution"))

class TicketDetail(TicketDetail):
    main = "general #history_tab more"

    general = dd.Panel("""
    general1:60 #votes.VotesByVotable:20
    description:30 comments.CommentsByRFC:30 faculties.DemandsByDemander #clocking.SessionsByTicket:20
    """, label=_("General"))

    general1 = """
    summary:40 id:6 deadline
    user:12 end_user:12 #faculty #topic
    site workflow_buttons
    """

    # history_tab = dd.Panel("""
    # changes.ChangesByMaster:50 #stars.StarsByController:20
    # """, label=_("History"), required_roles=dd.login_required(Triager))

    more = dd.Panel("""
    more1:60 faculties.AssignableWorkersByTicket:20
    upgrade_notes:20 LinksByTicket:20
    """, label=_("More"), required_roles=dd.login_required(Triager))

    more1 = """
    created modified ticket_type:10
    state priority project
    # standby feedback closed
    """

Tickets.detail_layout = TicketDetail()

