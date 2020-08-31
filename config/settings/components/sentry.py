# -*- coding: utf-8 -*-
import os

import raven

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': env('DJANGO_SENTRY_DSN', default=''),
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}
