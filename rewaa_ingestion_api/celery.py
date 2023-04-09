from celery import Celery
import os

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rewaa_ingestion_api.settings')

app = Celery('rewaa_ingestion_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)