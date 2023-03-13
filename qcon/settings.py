# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

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
from dotenv import load_dotenv

load_dotenv()

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

ELASTIC_APM_SERVICE_NAME = os.getenv('ELASTIC_APM_SERVICE_NAME')
ELASTIC_APM_SECRET_TOKEN = os.getenv('ELASTIC_APM_SECRET_TOKEN')
ELASTIC_APM_SERVER_URL = os.getenv('ELASTIC_APM_SERVER_URL')

API_KEY = os.environ.get('API_KEY')
GIT_TAG = os.getenv('GIT_TAG')
IMAGE_TAG = os.getenv('IMAGE_TAG')
IMAGE_TITLE = os.getenv('IMAGE_TITLE')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Defaults in `.secrets`
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv('DEBUG', False) == 'true'
ADMIN_ENABLED = os.getenv('DEBUG', False) == 'true'
LOGGING_LEVEL = 'INFO'

if DEBUG:
    POSTGRES_HOST = 'postgres'
    LOGGING_LEVEL = 'DEBUG'

ALLOWED_HOSTS = ['*']

CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'elasticapm.contrib.django',
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
    'channels',

    # Local Apps
    'api'
]

ELASTIC_APM = {
# "DEBUG": True,
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': ELASTIC_APM_SERVICE_NAME,

# Use if APM Server requires a secret token
'SECRET_TOKEN': ELASTIC_APM_SECRET_TOKEN,

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': ELASTIC_APM_SERVER_URL,
}

MIDDLEWARE = [
    'elasticapm.contrib.django.middleware.TracingMiddleware',
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

# WSGI_APPLICATION = 'qcon.wsgi.application'

# Channels
ASGI_APPLICATION = 'qcon.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': POSTGRES_HOST,
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
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
STATIC_ROOT = '/var/www/html/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'temp/')
# Qcon config
QCON = {
    'TEMP_FOLDER':
    os.path.join(BASE_DIR, 'temp', 'resource', 'tempfile') + os.path.sep,
    'TEMP_IMAGE_ROOT':
    os.path.join(BASE_DIR, 'temp', 'resource', 'tempfile', 'media') +
    os.path.sep,
    'RESPONDUS_XML_ROOT':
    os.path.join(BASE_DIR, 'temp', 'resource', 'xml') + os.path.sep,
    'XML_QUESTION_URL':
    '/ql/',
    'XML_QUESTION_ROOT':
    os.path.join(BASE_DIR, 'temp', 'resource', 'xml') + os.path.sep,
    'DEFAULT_IMAGE_FOLDER':
    '/assessment-assets/',
    'QCON_INSTALL_SCRIPT_ROOT':
    os.path.join(BASE_DIR, 'scripts', 'production') + os.path.sep,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format':
            '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'custom': {
            'format': '{levelname} {asctime} {name} {funcName} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'custom'
        },
        'elasticapm': {
            'level': LOGGING_LEVEL,
            'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
            'formatter': 'custom'
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'celery.log',
            'formatter': 'custom',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb
            'filters': ['require_debug_true']
        },
        'console_dev': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'dev.log',
            'formatter': 'custom',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb
            'filters': ['require_debug_true']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console','console_dev'],
            'level': 'ERROR',
            'propagate': False,
        },
        'api': {
            'handlers': ['console','console_dev','elasticapm'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        },
        # 'celery': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        'celery.task': {
            'handlers': ['console','console_dev','celery'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'api_v2.authentication.ExampleAuthentication',
    ]
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
