"""
Django settings for prueba project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'met#ex_@dvy&oa_*!z=j+z54b9_%sk0(z-$&#dfbn8x*)-^ha('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.tienda',
    'getpaid',
    'tbk',
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

ROOT_URLCONF = 'prueba.urls'

WSGI_APPLICATION = 'prueba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

##direccion de carpetas

from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('templates'),
)

MEDIA_ROOT = RUTA_PROYECTO.child('media')


MEDIA_URL = '/media/'


STATIC_ROOT = RUTA_PROYECTO.child('static')

STATIC_URL = '/static/'


GETPAID_BACKENDS = ('getpaid.backends.webpay',)
INSTALLED_APPS += GETPAID_BACKENDS

     
GETPAID_BACKENDS_SETTINGS = {
    'getpaid.backends.webpay': {
        'ASSETS_DIR': RUTA_PROYECTO.child('assets'),
        'STATIC_INBOUND_IP': '123.123.123.123',
        'CERTIFIED': True,
        'COMMERCE_ID_CLP': '527025007976',
        'COMMERCE_ID_USD': '527026003984',
        'TRANSBANK_PUBLIC_KEY': os.environ.get('TRANSBANK_PUBLIC_KEY'),
        'COMMERCE_PRIVATE_KEY': os.environ.get('COMMERCE_PRIVATE_KEY'),
    }
}



SITE_URL = 'http://localhost:8000/'