import datetime
from ..settings import *
class Site(Site):
    is_demo_site = True
    the_demo_date = datetime.date(2017, 3, 12)
    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.

        """
        super(Site, self).setup_plugins()
        self.plugins.ledger.configure(start_year=2017)
        # print "20151217 a", hash(self.plugins.ledger)

    
SITE = Site(globals())

DEBUG = True
