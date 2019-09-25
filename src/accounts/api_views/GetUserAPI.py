from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserSerializer, LoginSerializer


class GetUserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            'data': {
                'user': serializer.data,
                # 'featured': featured_serializer.data
            }
        }, status=status.HTTP_202_ACCEPTED)

    def get_object(self):
        return self.request.user
