from django.urls import path, include
from .views import *


urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('users/<int:pk>', UsersDetailAPIView.as_view()),
    path('posts/', PostsAPIView.as_view()),
    path('posts/<int:pk>', PostsDetailAPIView.as_view()),
]

    
