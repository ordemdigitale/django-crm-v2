web: gunicorn core.wsgi --log-file -
celery: celery worker -A core -l info -c 4