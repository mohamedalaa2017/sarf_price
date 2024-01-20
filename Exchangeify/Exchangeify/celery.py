# celery.py or wherever you have your Celery configuration
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Exchangeify.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('Exchangeify')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Use 'Africa/Cairo' as the Celery time zone
app.conf.timezone = 'Africa/Cairo'

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# Use the Django-celery-beat scheduler
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

# Set the broker URL for Redis
app.conf.broker_url = 'redis://localhost:6379/'

if __name__ == '__main__':
    app.start()
