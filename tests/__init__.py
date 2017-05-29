from unipath import Path

from lino.utils.pythontest import TestCase
from lino_presto import SETUP_INFO


class LinoTestCase(TestCase):
    # django_settings_module = "lino.projects.docs.settings.demo"
    project_root = Path(__file__).parent.parent


class PackagesTests(LinoTestCase):
    def test_01(self):
        self.run_packages_test(SETUP_INFO['packages'])


class SpecsTests(LinoTestCase):

    def test_presto(self):
        self.run_simple_doctests('docs/specs/test_presto.rst')

#     def test_psico(self):
#         self.run_simple_doctests('docs/specs/psico.rst')

#     def test_teams(self):
#         self.run_simple_doctests('docs/specs/teams.rst')


class Tutorials(LinoTestCase):

    def test_mini(self):
        self.run_django_manage_test("lino_presto/projects/std")
    

class DumpTests(LinoTestCase):
    def test_dump2py(self):
        for prj in ["lino_presto/projects/std"]:
            p = Path(prj)
            tmp = p.child('tmp').absolute()
            tmp.rmtree()
            self.run_django_admin_command_cd(p, 'dump2py', tmp)
            self.assertEqual(tmp.child('restore.py').exists(), True)

