from django.urls import path, include, re_path
from rest_framework import routers

from .api_views import PostModelViewSet, CommendsViewSet, FilesViewSet


urlpatterns = [
    path('<int:post_id>/', include(
        [
            path(
                'commends/',
                include(
                    [
                        path(
                            '',
                            CommendsViewSet.as_view(actions={
                                'post': 'create',
                            })
                        ),
                        path(
                            '<int:pk>/',
                            CommendsViewSet.as_view(actions={
                                'delete': 'destroy',
                            })
                        )
                    ]
                )

            ),
            re_path(
                r'^upload/(?P<filename>[^/]+)/$',
                FilesViewSet.as_view()
            ),
        ]
    )),
]

router = routers.DefaultRouter()
router.register('', PostModelViewSet, 'api-posts')

urlpatterns += router.urls
