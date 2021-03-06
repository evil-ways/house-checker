from houseChecker.settings.base import *

DEBUG = True

SECRET_KEY = 'SECRETKEYHERE'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'house_checker_dev',
        'USER': 'housecheckerdev',
        'PASSWORD': 'housecheckerdev',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


REDIS_URL = 'redis://localhost:6379/0'
CELERY_BROKER_URL = REDIS_URL
