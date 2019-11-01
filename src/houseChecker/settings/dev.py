from houseChecker.settings.base import *

DEBUG=True

SECRET_KEY = 'SECRETKEYHERE'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

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
