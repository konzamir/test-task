from celery import Task


class PublishPostsTask(Task):
    name = 'publish_posts'

    def run(self, *args, **kwargs):

        return f"Publish 0 posts!"
