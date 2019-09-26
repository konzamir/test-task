from django.contrib import admin
from .models import PostModel, CommendsModel, FilesModel


admin.site.register(PostModel)
admin.site.register(CommendsModel)
admin.site.register(FilesModel)
