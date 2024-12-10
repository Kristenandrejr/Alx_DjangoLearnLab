from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({'message': f'You are now following {user_to_follow.username}'}, status=200)
        return Response({'error': 'You cannot follow yourself.'}, status=400)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found.'}, status=404)

@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        if request.user != user_to_unfollow:
            request.user.following.remove(user_to_unfollow)
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=200)
        return Response({'error': 'You cannot unfollow yourself.'}, status=400)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found.'}, status=404)
