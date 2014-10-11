"""
Django settings for vkblind project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

import humanize

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Parse database configuration from $DATABASE_URL
DATABASES = {}
if os.getenv('APP_ENV') == 'production':
    DATABASES['default'] = dj_database_url.config()
else:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '208^z33+fzgskpk@nv1!w5jexz2)q)3yqsdz!mqc(d-v=jl2=-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vkblind',
    'vkblind.user_settings',
    'search',
    'groups',
    'feed',
    'ims',
    'social.apps.django_app.default'
)

AUTHENTICATION_BACKENDS = (
    'social.backends.vk.VKOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'vkblind.context_processors.user_settings',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SOCIAL_AUTH_VK_OAUTH2_KEY = os.getenv('VK_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = os.getenv('VK_SECRET')
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['wall', 'friends', 'offline', 'groups']

ROOT_URLCONF = 'vkblind.urls'

WSGI_APPLICATION = 'vkblind.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

humanize.i18n.activate('ru_RU')

APPEND_SLASH = False

