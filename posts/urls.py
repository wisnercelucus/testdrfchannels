from django.contrib import admin
from django.urls import path
from .views import PostListAPIView, PostDetail

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='posts-detail'),
]
