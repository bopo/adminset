# -*- coding: utf-8 -*-
INSTALLED_APPS += (
    'internal.payments',
    # 'payments',
)

PAYMENT_HOST = 'localhost:8000'
PAYMENT_USES_SSL = False
PAYMENT_MODEL = 'payments.Payment'
PAYMENT_VARIANTS = {
    'paypal': ('internal.payments.provider.paypal.PaypalProvider', {
        'client_id': 'client_id',
        'secret': 'secret',
    }),
    'dummy': ('internal.payments.provider.dummy.DummyProvider', {}),
}
