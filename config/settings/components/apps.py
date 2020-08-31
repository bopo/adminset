# -*- coding: utf-8 -*-
INSTALLED_APPS += (

    'service.setup',
    'service.navi',
    'service.cmdb',
    'service.configure',
    'service.accounts',
    'service.monitor',
    'service.appconf',
    'service.delivery',
    'service.elfinder',
    'service.branches',
    'service.mfile',
    'service.restful',

    # ------- extensions -------
    # 'django_celery_results',
    # 'django_celery_beat',
    'django_extensions',
    'import_export',
    'reversion',
    'imagekit',

    # ------- cleanup -------
    'django_cleanup',
    'storages',
)
