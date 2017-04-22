.. _presto.specs.psico:

=============================
Lino Psico : a first overview
=============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_psico
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_presto.projects.psico.settings.doctests')
    >>> from lino.api.doctest import *

**Lino Psico** (from Italian *psicologo*, psychologist) is a variant
of :ref:`presto` designed to be used in a center for
`sociopsychological
<https://en.wikipedia.org/wiki/Social_psychology>`_ consultations.

All :ref:`psico` application have a :xfile:`settings.py` module which
inherits from :mod:`lino_presto.projects.psico.settings`.

>>> settings.SETTINGS_MODULE
'lino_presto.projects.psico.settings.doctests'

Time tracking (Dienstleistungen)
================================

Lino Psico uses *time tracking* from :ref:`noi`, but unlike :ref:`noi`
it does not have the notion of *tickets*.  When a psychologist starts
a session, they don't specify a *ticket* but a *partner*.  The
clocking plugin has its own implementation specific to :ref:`psico`:

>>> dd.is_installed('clocking')
True

>>> dd.is_installed('tickets')
False

>>> dd.plugins.clocking
lino_presto.projects.psico.lib.clocking (extends_models=['Session'])

>>> print(dd.plugins.clocking.ticket_model)
<class 'lino_presto.projects.psico.lib.contacts.models.Partner'>

Partners
========

In Lino Psico, the partner is the central database object.  Many
statistical reports are based on attributes of partners.  

A partner is either a single person, a family, a household, or a group
of otherwise non-related partners having a same problem (called a
*therapeutic group*).

There might be (it is not yet decided) a differetiation between
"partner" and "dossier": a same partner can have more than one dossier
within the years. Currently they simply create the same partner a
second time (and add a field which connects them).

>>> print(settings.SITE.project_model)
<class 'lino_presto.projects.psico.lib.contacts.models.Partner'>

>>> dd.plugins.contacts
lino_presto.projects.psico.lib.contacts (extends_models=['Partner', 'Person', 'Company'])

>>> print([m.__name__ for m in rt.models_by_base(rt.models.contacts.Partner)])
['Company', 'Partner', 'Person', 'Household']


Therapeutical groups
====================

>>> dd.plugins.lists
lino_presto.projects.psico.lib.lists (extends_models=['List'])

>>> rt.show(lists.Lists)
=========== ========================= ===========
 Reference   Description               List Type
----------- ------------------------- -----------
             *Women's group 2014*
             *Men's group 2014*
             *Children's group 2014*
             *Women's group 2015*
             *Men's group 2015*
             *Children's group 2015*
             *Women's group 2016*
             *Men's group 2016*
             *Children's group 2016*
=========== ========================= ===========
<BLANKLINE>
