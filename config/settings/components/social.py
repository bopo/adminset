# -*- coding: utf-8 -*-
# 社会化登录配置

INSTALLED_APPS += ('internal.socialauth',)

AUTHENTICATION_BACKENDS = (
    'internal.socialauth.contrib.core.backends.qq.QQOAuth2',  # QQ的功能
    'internal.socialauth.contrib.core.backends.weibo.WeiboOAuth2',  # 微博的功能
    'internal.socialauth.contrib.core.backends.wechat.WeixinOAuth2',  # 这个是导入微信的功能
    'internal.socialauth.contrib.core.backends.wechat.WeixinOAuth2APP',  # 这个是导入微信的功能
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'internal.socialauth.contrib.core.backends.qq.QQOAuth2',  # QQ的功能
    'internal.socialauth.contrib.core.backends.weibo.WeiboOAuth2',  # 微博的功能
    'internal.socialauth.contrib.core.backends.wechat.WeixinOAuth2',  # 这个是导入微信的功能
    'internal.socialauth.contrib.core.backends.wechat.WeixinOAuth2APP',  # 这个是导入微信的功能
)

SOCIAL_AUTH_PIPELINE = (
    'internal.socialauth.contrib.core.pipeline.social_auth.social_details',
    'internal.socialauth.contrib.core.pipeline.social_auth.social_uid',
    'internal.socialauth.contrib.core.pipeline.social_auth.social_user',
    'internal.socialauth.contrib.core.pipeline.user.get_username',
    'internal.socialauth.contrib.core.pipeline.user.create_user',
    'internal.socialauth.contrib.core.pipeline.social_auth.associate_user',
    'internal.socialauth.contrib.core.pipeline.social_auth.load_extra_data',
    'internal.socialauth.contrib.core.pipeline.user.user_details',
    'internal.socialauth.contrib.core.pipeline.social_auth.associate_by_email',
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
