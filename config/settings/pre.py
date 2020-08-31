# -*- coding: utf-8 -*-
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE
from split_settings.tools import include

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    # 'components/auth.py',
    # 'components/docs.py',
    'components/suit.py',
    'components/test.py',
    'components/logs.py',

    # 'components/pays.py',
    'components/static.py',
    # 'components/social.py',
    # 'components/sentry.py',
    'components/celery.py',
    # 'components/search.py',
    # 'components/notify.py',
    'components/const.py',
    # 'components/db.py',
    # 'components/admin.py',
    # 'components/const.py',
    # 'components/cache.py',
    # 'components/email.py',
    'components/thumb.py',
    # 'components/store.py',
    # optional('components/debug.py'),
)

# INSTALLED_APPS += ['django_cleanup.apps.CleanupConfig']
DEBUG = env('DJANGO_DEBUG', default=False)
STATIC_ROOT = env('DJANGO_STATIC_ROOT',
                  default=str(ROOT_DIR.path('assets/static')))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME', default='ponder'),
        'USER': env('POSTGRES_USER', default='ponder'),
        'PASSWORD': env('POSTGRES_PASS', default='ponder'),
        'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env('POSTGRES_PORT', default='5432'),
        'OPTIONS': {
            'isolation_level': ISOLATION_LEVEL_SERIALIZABLE,
            'client_encoding': 'UTF8',
        },
        'timezone': 'UTC',
    }
}
