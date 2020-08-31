# -*- coding: utf-8 -*-
# 极光 API 参数
JPUSH_APPKEY = env('DJANGO_JPUSH_APPKEY', default='')
JPUSH_SECRET = env('DJANGO_JPUSH_SECRET', default='')
JPUSH_OPTION = {
    "apns_production": env('DJANGO_JPUSH_PRODUCTION', default=False),
    "time_to_live": 86400,
    "sendno": 12345,
}

# 微信公众号的 Token
WECHAT_TOKEN = env('DJANGO_WECHAT_TOKEN', default='')

# 微信登录 API 参数
WECHAT_LOGIN_APPKEY = env('DJANGO_WECHAT_LOGIN_APPKEY', default='')
WECHAT_LOGIN_SECRET = env('DJANGO_WECHAT_LOGIN_SECRET', default='')

# 微信公众号 API 参数
WECHAT_MPS_APPKEY = env('DJANGO_WECHAT_MPS_APPKEY', default='')
WECHAT_MPS_SECRET = env('DJANGO_WECHAT_MPS_SECRET', default='')
WECHAT_MPS_OPTION = {}

# 微信小程序 API 参数
WECHAT_APP_APPKEY = env('DJANGO_WECHAT_APP_APPKEY', default='')
WECHAT_APP_SECRET = env('DJANGO_WECHAT_APP_SECRET', default='')
WECHAT_APP_OPTION = {}

# 微信支付 API 参数
WECHAT_PAY_APIKEY = env('DJANGO_WECHAT_PAY_APIKEY', default='')
WECHAT_PAY_MCH_ID = env('DJANGO_WECHAT_PAY_MCH_ID', default='')
WECHAT_PAY_OPTION = {}

# 支付宝支付 API 参数
ALIPAY_PAY_APIKEY = env('DJANGO_ALIPAY_PAY_APIKEY', default='')
ALIPAY_PAY_SECRET = env('DJANGO_ALIPAY_PAY_SECRET', default='')
ALIPAY_PAY_OPTION = {}

CERTIFICATES_PATH = env('DJANGO_CERTIFICATES_PATH',
                        default=ROOT_DIR.path('assets/certs'))

TAGGIT_FOR_MODELS = [
    'resource.Category',
]
