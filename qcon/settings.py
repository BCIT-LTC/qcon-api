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

API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
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

DEBUG = os.getenv('DEBUG', False) == 'True'
ADMIN_ENABLED = os.getenv('DEBUG', False) == 'True'

if DEBUG:
    POSTGRES_HOST = 'postgres'

ALLOWED_HOSTS = ['*']

CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'channels',
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
    # 'django_q',
    'drf_spectacular',

    # Local Apps
    # 'api_v2.apps.ApiV2Config'
    'api_v2',
    'api_v3'
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

# WSGI_APPLICATION = 'qcon.wsgi.application'

# Channels
ASGI_APPLICATION = 'qcon.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '/tmp/database',
#     }
# }

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
    'disable_existing_loggers': False,
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
            'format': '{levelname} {asctime} {file} {name} {funcName} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'custom'
        },
        # 'file': {
        #     'level': 'ERROR',
        #     'class': 'logging.FileHandler',
        #     'filename': '/code/log/main.log',
        #     'formatter': 'custom'
        # },
        # 'file': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'filename': '/code/log/main.log',
        #     'when': 'D',  # daily 'D', you can use 'midnight' as well
        #     'backupCount': 7,  # 7 days backup
        #     'formatter': 'custom'
        # }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'api_v2': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'api_v3': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
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
    ],
    'DEFAULT_SCHEMA_CLASS':
    'drf_spectacular.openapi.AutoSchema',
}

# Q_CLUSTER = {
#     'name': 'myproject',
#     'workers': 8,
#     'recycle': 500,
#     'timeout': 300,
#     'retry': 301,
#     'max_attempts': 1,
#     'compress': True,
#     'save_limit': 250,
#     'queue_limit': 500,
#     'cpu_affinity': 1,
#     'label': 'Django Q',
#     'orm': 'default'
# }

SPECTACULAR_SETTINGS = {
    # 'VERSION': '1.0.0',
    'TITLE': 'Qcon API',
    'DESCRIPTION':
    'RESTful API to convert word documents to LMS compliant format',
    "COMPONENT_SPLIT_REQUEST": True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True
    }
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