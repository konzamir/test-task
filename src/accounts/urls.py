from django.urls import path, include
from .api_views import RegisterAPI, LoginAPI, GetUserAPI, LogoutAPIView


urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', LogoutAPIView.as_view(), name='knox-logout'),
    path('/', include('knox.urls')),
    path('user/', GetUserAPI.as_view()),
]
