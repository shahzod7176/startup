import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('root')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    broker_connection_retry_on_startup=True,
    timezone='Asia/Tashkent'
)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
