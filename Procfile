
worker: DJANGO_DEBUG=false celery -A config worker -l info
beater: DJANGO_DEBUG=false celery -A config beat -l info
flower: DJANGO_DEBUG=false celery -A config flower
minios: minio server ./runtime/data
server: python manage.py runserver_plus
# rediss: redis-server

# server: gunicorn config.wsgi:application -k egg:meinheld#gunicorn_worker -w 4 -b 0.0.0.0:5000
# search: elasticsearch -v
# daphne: daphne -b 0.0.0.0 -p 8080 config.asgi:application
# sentry: sentry start
