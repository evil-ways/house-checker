import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import dj_database_url
from decouple import config

from houseChecker.settings.base import *

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}

REDIS_URL = config('REDIS_URL')
CELERY_BROKER_URL = CELERY_RESULT_BACKEND = REDIS_URL

sentry_sdk.init(dsn=config('SENTRY_URL', cast=str), integrations=[DjangoIntegration()])
