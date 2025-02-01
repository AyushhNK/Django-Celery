import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Celery.settings")

app = Celery("Celery")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from each installed app
app.autodiscover_tasks()
