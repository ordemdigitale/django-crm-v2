web: gunicorn core.wsgi --log-file -
celery: celery -A core worker -l info --pool=solo
#celery: celery worker -A core -l info -c 4