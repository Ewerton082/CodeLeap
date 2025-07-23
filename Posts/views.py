from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Posts, Like
from .serializers import PostsSerializer, PostSerializerEdit, LikeCreateSerializer, LikeSerializer, LikeDeleteSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostDetailEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostSerializerEdit
        return PostsSerializer


class LikeCreate(APIView):
    def post(self, request):
        serializer = LikeCreateSerializer(data=request.data)
        if serializer.is_valid():
            like = serializer.save()
            return Response(LikeSerializer(like).data, status=201)
        return Response(serializer.errors, status=400)


class LikeDelete(APIView):
    def delete(self, request, post_id, user_id):
        data = {'post': post_id, 'user': user_id}

        serializer = LikeDeleteSerializer(data=data)
        if serializer.is_valid():
            like = Like.objects.get(user=serializer.validated_data['user'], post=serializer.validated_data['post'])
            like.delete()
            return Response({"detail": "Like removido com sucesso."}, status=204)
        return Response(serializer.errors, status=400)
