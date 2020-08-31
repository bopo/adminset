# -*- coding: utf-8 -*-
INSTALLED_APPS += (
    "django_celery_results",
    'django_celery_beat',
)

CELERY_BROKER_URL = env('DJANGO_CELERY_BROKER_URL', default='')
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

# CELERY_CACHE_BACKEND = 'django-cache'
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
