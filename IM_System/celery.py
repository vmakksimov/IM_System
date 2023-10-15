import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IM_System.settings')
app = Celery('IM_System')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()