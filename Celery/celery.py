# Celery/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery.settings')

app = Celery('Celery')

# load settings from Django settings, using CELERY_ namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks from all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
