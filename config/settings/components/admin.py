# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'admin_tools',
    'admin_tools.dashboard',
    'admin_tools.menu',
    'admin_tools.theming',
] + INSTALLED_APPS

# INSTALLED_APPS = [
#                      'fluent_dashboard',
#                      'admin_tools',
#                      'admin_tools.theming',
#                      'admin_tools.menu',
#                      'admin_tools.dashboards',
#                      'django.contrib.admin',
#                  ] + INSTALLED_APPS + [
#                      # 'dashboardmods',
#                  ]
# ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboards.FluentIndexDashboard'
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboards.FluentAppIndexDashboard'
# ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': (),
# #         'OPTIONS': {
# #             'loaders': (
# #                 'admin_tools.template_loaders.Loader',  # Add this line!
# #             ),
# #         }
# #     }
# # ]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'loaders': (
#                 'admin_tools.template_loaders.Loader',  # Add this line!
#             ),
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# FLUENT_DASHBOARD_APP_GROUPS = (
#     (_('CMS'), {
#         'models': (
#             'cms.*',
#             'pages.*',
#             'fiber.*',
#         ),
#         'module': 'CmsAppIconList',
#         'collapsible': False,
#     }),
#     (_('Interactivity'), {
#         'models': (
#             'django.contrib.comments.*',
#             'form_designer.*'
#             'threadedcomments.*',
#             'zinnia.*',
#         ),
#     }),
#     (_('Administration'), {
#         'models': (
#             'django.contrib.auth.*',
#             'django.contrib.sites.*',
#             'google_analytics.*',
#             'registration.*',
#         ),
#     }),
#     (_('Applications'), {
#         'models': ('*',),
#         'module': 'AppList',
#         'collapsible': True,
#     }),
# )
