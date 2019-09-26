from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class PostModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=False, null=False, default='')
    user = models.ForeignKey(to='accounts.UserModel', on_delete=models.DO_NOTHING, blank=True, null=True)
    pub_time = models.DateTimeField(db_index=True, blank=True, null=True)
    was_checked = models.BooleanField(db_index=True, default=False)
    was_published = models.BooleanField(db_index=True, default=False)

    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.name


class CommendsModel(MPTTModel):
    text = models.TextField(blank=False, null=False, default='')
    user = models.ForeignKey(to='accounts.UserModel', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(to='PostModel', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # class MPTTMeta:
    #     order_insertion_by = ['text']

    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.post.name}'


class FilesModel(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=128)
    post = models.ForeignKey(to='PostModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post.name}"
