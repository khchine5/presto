from lino.invlib.ns import ns
ns.setup_from_tasks(
    globals(), "lino_presto",
    languages="en de fr et".split(),
    tolerate_sphinx_warnings = False,
    blogref_url='http://luc.lino-framework.org',
    revision_control_system='git',
    # locale_dir='lino_presto/lib/presto/locale',
    cleanable_files=['docs/api/lino_presto.*'],
    demo_projects=[
        'lino_presto.projects.std.settings.demo',
        'lino_presto.projects.psico.settings.demo'])
