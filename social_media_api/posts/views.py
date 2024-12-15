# posts/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    ["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"]
    ["Post.objects.filter(author__in=following_users).order_by", "following.all()"]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# New Like Functionality
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if user has already liked the post
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a notification
    notification = Notification.objects.create(
        recipient=post.user,
        actor=user,
        verb="liked your post",
        target=post,
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=post.pk
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Delete the like
    like.delete()

    # Optional: Remove the notification related to the like
    notification = Notification.objects.filter(actor=user, target=post).first()
    if notification:
        notification.delete()

    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
