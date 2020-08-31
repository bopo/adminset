# -*- coding: utf-8 -*-
INSTALLED_APPS += [
    "django_thumbor",
]

# The host serving the thumbor resized img
THUMBOR_SERVER = 'http://103.200.97.197:8888/'

# The prefix for the host serving the original img
# This must be a resolvable address to allow thumbor to reach the img
THUMBOR_MEDIA_URL = 'http://103.200.97.197:8888/media'

# If you want the static to be handled by django thumbor
# default as False, set True to handle it if you host your statics
THUMBOR_STATIC_ENABLED = False

# The prefix for the host serving the original static img
# this must be a resolvable address to allow thumbor to reach the img
THUMBOR_STATIC_URL = 'http://103.200.97.197:8888/static'

# The same security key used in the thumbor service to
# match the URL construction
THUMBOR_SECURITY_KEY = ''

# Default arguments passed to the `generate_url` helper or
# the `thumbor_url` templatetag
THUMBOR_ARGUMENTS = {}

# An alias represents a named set of arguments to the generate_url function
# or thumbor_url template tag. Use it to share general thumbnail
# configurations without repeating yourself.
THUMBOR_ALIASES = {
    'thumb-square': {
        'width': 300,
        'height': 300,
        'filters': ['brightness(10)']
    }
}
