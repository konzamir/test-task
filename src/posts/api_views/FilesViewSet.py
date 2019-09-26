from posts.models import FilesModel
from posts.serializers import FilesSerializer

from rest_framework import status, mixins, views, parsers
from rest_framework.response import Response


class FilesViewSet(views.APIView, mixins.CreateModelMixin):
    parser_classes = [
        parsers.FileUploadParser
    ]

    def post(self, request, post_id=None, filename=None, *a, **kw):
        if not post_id:
            return Response({
                'data': None,
                'error': 'Post id must be provided!'
            }, status.HTTP_403_FORBIDDEN)

        file_obj = request.data['file']
        data = {
            "file": file_obj,
            "name": filename,
            "post":post_id
        }

        serializer = FilesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({
            'data': serializer.data
        }, status=status.HTTP_204_NO_CONTENT, headers=headers)
