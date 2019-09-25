from django.urls import path, include
from .api_views import RegisterAPI, LoginAPI, GetUserAPI, LogoutAPIView


urlpatterns = [
    path('auth/register/', RegisterAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/logout/', LogoutAPIView.as_view(), name='knox-logout'),
    path('auth', include('knox.urls')),
    path('auth/user/', GetUserAPI.as_view()),
]
