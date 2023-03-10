from django.urls import path

from .views import (
    UserListView,
    PostListView,
    PostDetailsView,
    UserDetailsView,
    PostCreateView,
    PostDeleteView,
)

app_name = "blog_django_posts"

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('users/<int:pk>/', UserDetailsView.as_view(), name="user_details"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetailsView.as_view(), name="post_details"),
    path('post-creation/', PostCreateView.as_view(), name="post_creation"),
    path('posts/<int:pk>/delete-post/', PostDeleteView.as_view(), name="post_delete"),
]
