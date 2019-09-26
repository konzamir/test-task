from django.urls import path
from rest_framework import routers

from .api_views import PostModelViewSet


urlpatterns = []

router = routers.DefaultRouter()
router.register('', PostModelViewSet, 'api-posts')

urlpatterns += router.urls
