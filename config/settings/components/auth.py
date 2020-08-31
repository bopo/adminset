# -*- coding: utf-8 -*-
ANONYMOUS_USER_ID = -1

# AUTHENTICATION_BACKENDS = (
# 'django.contrib.auth.backends.ModelBackend',
# 'service.backends.passport.backends.PassportBackend',
# 'service.backends.passport.backends.VerifyBackend',
# )

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]