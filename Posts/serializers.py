from rest_framework import serializers
from .models import Posts, Like


class PostsSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'user', 'title', 'content', 'likes_count', 'created_datetime']
        read_only_fields = ["id"]

    def get_likes_count(self, obj):
        return obj.like_set.count()


class PostSerializerEdit(PostsSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'user', 'title', 'content', 'likes_count', 'created_datetime']
        read_only_fields = ["id", "user"]



class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'username', 'post', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']
