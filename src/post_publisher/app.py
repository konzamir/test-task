from __future__ import absolute_import, unicode_literals
from celery import Celery

from post_publisher.tasks import PublishPostsTask


app = Celery('celery_app')
app.config_from_object('main.settings', namespace='CELERY')

app.tasks.register(PublishPostsTask())
