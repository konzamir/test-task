from django.urls import path
from rest_framework import routers

from .api_views import PostModelViewSet, CommendsViewSet, FilesViewSet


urlpatterns = [
    path(
        '<int:post_id>/commends/',
        CommendsViewSet.as_view(actions={
            'post': 'create',
        })
    ),
    path(
        '<int:post_id>/commends/<int:pk>/',
        CommendsViewSet.as_view(actions={
            'delete': 'destroy',
        })
    ),

]

router = routers.DefaultRouter()
router.register('', PostModelViewSet, 'api-posts')

urlpatterns += router.urls
