# -*- coding: utf-8 -*-
import os

import environ

ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(ROOT_DIR.path('.env').root)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#b68qv#(v-g26k3qt_-1ufg-prvsw2p)7@ctea*n!36-w23bv1'
SECRET_KEY = env('DJANGO_SECRET_KEY', default=SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

print('.env >> ', ROOT_DIR.path('.env').root)
print('DJANGO_SECRET_KEY', env('DJANGO_SECRET_KEY'))
print('DJANGO_DEBUG', env('DEBUG'))

SITE_ID = env.int('DJANGO_SITE_ID', default=1)

ALLOWED_HOSTS = [
    '*',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'django.contrib.flatpages',
]

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'config', 'fixtures'),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'config.middleware.BetterExceptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'zh-hans'
LANGUAGE_CODE = env('DJANGO_LANGUAGE_CODE', default='zh-hans')

# TIME_ZONE = 'UTC'
TIME_ZONE = env('DJANGO_TIME_ZONE', default='Asia/Shanghai')

# USE_I18N = True
USE_I18N = env('DJANGO_USE_I18N', default=True)

# USE_L10N = True
USE_L10N = env('DJANGO_USE_L10N', default=True)

# USE_TZ = True
USE_TZ = env('DJANGO_USE_TZ', default=True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT_DIR, 'templates'),],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'debug':
                True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'admin_tools.template_loaders.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

HASHID_FIELD_SALT = SECRET_KEY

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
