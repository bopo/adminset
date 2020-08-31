import configparser
import os

from celery import Celery

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.pre')
app = Celery('devops')

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'adminset.conf'))
redis_host = config.get('redis', "redis_host")
redis_port = config.get("redis", "redis_port")
redis_db = config.get('redis', "redis_db")
redis_password = config.get('redis', "redis_password")

if redis_password:
    app.conf.broker_url = 'redis://:{0}@{1}:{2}/{3}'.format(redis_password, redis_host, redis_port, redis_db)
else:
    app.conf.broker_url = 'redis://{0}:{1}/{2}'.format(redis_host, redis_port, redis_db)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
