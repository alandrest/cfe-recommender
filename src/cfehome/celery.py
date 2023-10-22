import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome')

# CELERY_, the namespace as the  const variable first part at the settings.py
app.config_from_object("django.conf:settings",namespace = 'CELERY')
# one more option: use instead (if not using Django):
# app.conf.broker_url = ''
# app.conf.result_backend='django-db'

app.autodiscover_tasks()