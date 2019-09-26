from posts.models import CommendsModel
from posts.serializers import CommendSerializer

from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response


class CommendsViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = CommendsModel.objects.all()
    serializer_class = CommendSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def create(self, request, post_id=None, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, post_id=None, pk=None, *args, **kwargs):
        instance = CommendsModel.objects.get(pk=pk)
        self.perform_destroy(instance)

        return Response({
            'data': None
        }, status=status.HTTP_204_NO_CONTENT)
