from django.urls import path, include
from .views import *



urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('users/', UsersAPIView.as_view()),
    path('users/<int:pk>', UsersDetailAPIView.as_view()),
]

    
