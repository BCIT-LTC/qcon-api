"""
Django settings for qcon project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd8&z=vqy5b#lu0=an1xx9b_7n480af=-gdnqwqvtrs&d6el9=('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'django_q',
    'drf_spectacular',

    # Local Apps
    # 'api_v1.apps.ApiV1Config'
    'api_v1'
    # 'django_api_v1.api_v1.apps.ApiV1Config'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qcon.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'qcon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'temp/')
# Qcon config
QCON = {
    'TEMP_FOLDER': os.path.join(BASE_DIR, 'temp', 'resource', 'tempfile') + os.path.sep,
    'TEMP_IMAGE_ROOT': os.path.join(BASE_DIR, 'temp', 'resource', 'tempfile', 'media') + os.path.sep,
    'RESPONDUS_XML_ROOT': os.path.join(BASE_DIR, 'temp', 'resource', 'xml') + os.path.sep,
    'XML_QUESTION_URL': '/ql/',
    'XML_QUESTION_ROOT': os.path.join(BASE_DIR, 'temp', 'resource', 'xml') + os.path.sep,
    'DEFAULT_IMAGE_FOLDER': '/assessment-assets/',
    'QCON_INSTALL_SCRIPT_ROOT': os.path.join(BASE_DIR, 'scripts', 'production') + os.path.sep,
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        # 'error': {
        #     'level': 'ERROR',
        #     'class': 'logging.FileHandler',
        #     'filename': '/code/log/error.log',
        #     'formatter': 'verbose'
        # },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/code/log/error.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['warning', 'console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'api_v1': {
            'handlers': ['console'],
            'level': 'INFO',
            # 'filters': ['special']
        }
    },
}


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


Q_CLUSTER = {
    'name': 'myproject',
    'workers': 8,
    'recycle': 500,
    'timeout': 300,
    'retry': 301,
    'max_attempts': 1,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'orm': 'default'
}


SPECTACULAR_SETTINGS = {

    'VERSION': '1.0.0',
    'TITLE': 'Qcon API',
    'DESCRIPTION': 'RESTful API to convert word documents to LMS compliant format',
    "COMPONENT_SPLIT_REQUEST" : True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True
    }
}
