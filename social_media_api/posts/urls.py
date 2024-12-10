from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Include the original routes for posts and comments
    path('', include(router.urls)),

    # New route for user feed
    path('feed/', user_feed, name='user_feed'),
]
