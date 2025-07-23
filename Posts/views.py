from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Posts, Like
from .serializers import PostsSerializer,PostSerializerEdit, LikeSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostDetailEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostSerializerEdit
        return PostsSerializer
