import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import dj_database_url
from decouple import config

from houseChecker.settings.base import *

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}

REDIS_URL = 'redis://h:p6d3c0ed96ec492545ce8adf1b52be97072ff7b7d08b7ed7fd129a229b22606bb@ec2-34-233-248-192.compute-1.amazonaws.com:20649'
CELERY_BROKER_URL = CELERY_RESULT_BACKEND = REDIS_URL

sentry_sdk.init(dsn=config('SENTRY_URL', cast=str), integrations=[DjangoIntegration()])
