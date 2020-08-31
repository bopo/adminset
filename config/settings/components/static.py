# -*- coding: utf-8 -*-
# 静态文件配置项
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')
THUMB_ROOT = str(ROOT_DIR.path('assets/media/thumb'))
MEDIA_ROOT = str(ROOT_DIR.path('assets/media'))
MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')
ADMIN_MEDIA_PREFIX = MEDIA_URL

# STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(ROOT_DIR.path('assets/static')))
