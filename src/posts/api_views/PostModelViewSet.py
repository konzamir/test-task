from django.conf import settings

from posts.helpers import get_full_post_data
from posts.models import PostModel
from posts.pagination import CustomPaginator
from posts.serializers import PostSerializer

from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response


class PostModelViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    pagination_class = CustomPaginator

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(
            queryset=PostModel.objects.all()
        )
        serialized_data = self.get_serializer(queryset, many=True).data

        full_data = [get_full_post_data(x) for x in serialized_data]

        return Response({
            'data': full_data,
            'pagination': {
                'total_count': PostModel.objects.all().count(),
                'per_page': settings.POSTS_PER_PAGE
            }
        }, status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk:
            post = PostModel.objects.get(pk=pk)
            post = self.get_serializer(post, many=False).data

            return Response({
                'data': get_full_post_data(post)
            }, status.HTTP_200_OK)
        else:
            return Response({
                'data': None,
                'error': 'No pk were founded!'
            }, status.HTTP_417_EXPECTATION_FAILED)
