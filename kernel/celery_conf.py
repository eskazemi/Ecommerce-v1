from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kernel.settings')

celery_app = Celery('kernel')

celery_app.autodiscover_tasks()

celery_app.conf.broker_url = "amqp://"
celery_app.conf.result_backend = "rpc://"
celery_app.conf.task_serializer = "json"
celery_app.conf.result_serializer = "pickle"
celery_app.conf.accept_content = ["json", "pickle"]
celery_app.conf.result_expire = timedelta(days=1)
celery_app.conf.task_always_eager = False  # task run to block client
celery_app.conf.worker_prefetch_multiplier = 2
