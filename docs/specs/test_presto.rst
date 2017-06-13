.. _lino.tested.presto:

==================================
Miscellaneous tests in Lino Presto
==================================

.. to run only this test:
   
    $ python setup.py test -s tests.SpecsTests.test_presto
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_presto.projects.std.settings.doctests')
    >>> from lino.api.doctest import *

Test whether the bootstrap3 user interface works:

>>> url = '/bs3/products/Products'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print res.status_code
200

