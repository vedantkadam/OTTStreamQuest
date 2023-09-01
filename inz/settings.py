"""
Django settings for inz project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dm7)1wl2txoqck3#tn5_t3gdbjd68q=khb^&fz(juo$4&tmpyy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    'crispy_bootstrap4',
    'movie',
    'register.apps.RegisterConfig',
    'rating.apps.RatingConfig',
    "django_pivot",
    'django_extensions',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'inz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'inz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "djongo",
#         "CLIENT": {
#             'name': 'ott_plat',
#             'host': 'mongodb+srv://'+WE_CHAT_USR+':'+WE_CHAT_PASS+'@cluster0.1yefb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
#             #'host': 'mongodb+srv://'+WE_CHAT_USR+':'+WE_CHAT_PASS+'@cluster0.1yefb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
#             'username': WE_CHAT_USR,
#             'password': WE_CHAT_PASS,
#             "authMechanism": "SCRAM-SHA-1",
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

TIME_ZONE = 'UTC'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#LOCALIZATIONS
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
USE_I18N = True

from django.utils.translation import gettext_lazy as _
LANGUAGE_CODE='en'

LANGUAGES = (
    ('en', _('English')),
    ('pl', _('Polish')),
)

LANGUAGE_CODE='en'

#SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vedantkadam@student.sfit.ac.in'
EMAIL_HOST_PASSWORD = 'albsbwcscidvgyqp'
# EMAIL_ACTIVE_FIELD = 'is_active'

# django_heroku.settings(locals())

RAZOR_KEY_ID ='rzp_test_Q8AZkEbm7RUitk'
RAZOR_KEY_SECRET ='Esu9mt6ZyXxjrEgnqKKJTjLn'