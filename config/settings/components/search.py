# -*- coding: utf-8 -*-
INSTALLED_APPS += (
    'haystack',
    'drf_haystack',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE':
            'haystack.backends.elasticsearch5_backend.Elasticsearch5SearchEngine',
        'URL':
            'http://127.0.0.1:9200/',
        'INDEX_NAME':
            'haystack',
    },
}
