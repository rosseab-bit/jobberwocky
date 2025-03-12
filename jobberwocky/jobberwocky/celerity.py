# jobberwocky/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobberwocky.settings')

app = Celery('jobberwocky')

# Usar la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todos los módulos de aplicaciones registradas
app.autodiscover_tasks()

