from celery import Task

from django.db.models import Q
from django.utils import timezone

from posts.models import PostModel


class PublishPostsTask(Task):
    name = 'publish_posts'
    pack_count = 500

    def run(self, *args, **kwargs):
        query = PostModel.objects.filter(
            Q(was_checked=True) & Q(was_published=False) &
            (Q(pub_time__lte=timezone.now().date()) | Q(pub_time__isnull=True))
        )

        return f"Publish 0 posts!"
