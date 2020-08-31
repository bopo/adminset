# -*- coding: utf-8 -*-

from split_settings.tools import include, optional

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    'components/auth.py',
    # 'components/docs.py',
    # 'components/suit.py',
    # 'components/test.py',
    'components/logs.py',
    # 'components/ldap.py',

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
    # 'components/thumb.py',
    # 'components/store.py',
    optional('components/debug.py'),
)

# DEBUG = env('DEBUG', default=True)
# DEBUG = env.bool('DJANGO_DEBUG', default=True)
# DEBUG = True
# INSTALLED_APPS += ['django_cleanup.apps.CleanupConfig']

print('DEBUG:', DEBUG)

# if DEBUG:
#     STATICFILES_DIRS = [
#         str(ROOT_DIR.path('assets/static')),
#     ]

STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(ROOT_DIR.path('assets/static')))

# if env("TEST", default=False):
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    },
}

# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': env('POSTGRES_NAME', default='ponder'),
#             'USER': env('POSTGRES_USER', default='ponder'),
#             'PASSWORD': env('POSTGRES_PASS', default='87225300'),
#             'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
#             'PORT': env('POSTGRES_PORT', default='5432'),
#             'OPTIONS': {
#                 'isolation_level': ISOLATION_LEVEL_SERIALIZABLE,
#                 'client_encoding': 'UTF8',
#             },
#             'timezone': 'UTC',
#         }
#     }
