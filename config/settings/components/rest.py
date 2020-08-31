# -*- coding: utf-8 -*-
INSTALLED_APPS += (
    'corsheaders',
    'django_filters',
    'rest_framework',
    # 'rest_framework_api_key',
    'rest_framework.authtoken',
)

REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'service.backends.internal.exception.custom_exception_handler',
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPaginationg',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'service.backends.internal.pagination.CustomPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
        # 'rest_framework_xml.renderers.XMLRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework_xml.parsers.XMLParser',
    # ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'SERIALIZER_EXTENSIONS': {
        'USE_HASH_IDS': True,
        'HASH_IDS_SOURCE': 'service.backends.internal.HASH_IDS'
    },
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework_api_key.permissions.HasAPIKey",
    # ],
    'DATETIME_FORMAT':
        '%Y-%m-%d %H:%M:%S',
    'PAGE_SIZE':
        20,
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )
}

REST_FRAMEWORK_EXTENSIONS = {'DEFAULT_USE_CACHE': 'default'}

CORS_ORIGIN_ALLOW_ALL = True
ACCOUNT_EMAIL_VERIFICATION = None
OLD_PASSWORD_FIELD_ENABLED = True
