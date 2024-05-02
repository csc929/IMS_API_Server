"""
Django settings for IMS_API_Server project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
from unittest.mock import DEFAULT
import uuid

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = uuid.uuid4().hex

# Network & Paths

# SECURITY WARNING: don't run with debug turned on in production!
TESTING_MODE = True  
DEBUG = TESTING_MODE
# ROOT_URLCONF = 'StockManagement.urls'
# WSGI_APPLICATION = 'StockManagement.wsgi.application'
X_FRAME_OPTIONS = 'DENY'
if not TESTING_MODE:  
    SECURE_HSTS_SECONDS = 30 # 30s for Testing. Set to more appropriate in production
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.2.190' if TESTING_MODE else '']
CORS_ALLOW_ALL_ORIGINS = True  # only set True for testing purposes
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ['http://localhost:5173','http://127.0.0.1:5173','http://192.168.2.190:5173' if TESTING_MODE else '']
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173','http://127.0.0.1:5173','http://192.168.2.190:5173' if TESTING_MODE else '']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'IMS_Control.apps.IMSControlConfig',
    'Accounts.apps.AccountsConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_q'
]

# # # rest framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'IMS_Control.custom_permissions.AccessPermissions',
    ],
    # 'PAGE_SIZE': 5,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
]

ROOT_URLCONF = 'IMS_API_Server.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

# # # django_q

Q_CLUSTER = {
    'name': 'InventoryManagementSystem',
    'daemonize_workers': True,
    'compress': True,
    'workers': 2,
    'recycle': 5000,
    'timeout': 99999,
    'retry': 100000,
    'queue_limit': 4,
    'bulk': 1,
    'orm': 'default',
    'sync': False,  # Set True to debug in sync mode.
    'guard_cycle': 5,
    'cpu_affinity': 1,
    'catch_up': True
}

WSGI_APPLICATION = 'IMS_API_Server.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ims_prod',
            'USER': 'admin',
            'PASSWORD': 'Admin@123',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))