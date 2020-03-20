web:  cd src && gunicorn houseChecker.wsgi:application --log-file -
worker: cd src && celery worker --app=houseChecker.celery:app