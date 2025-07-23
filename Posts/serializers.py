from rest_framework import serializers

from .models import Posts, Like
from Users.models import User


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
        fields = ['id', 'user', 'post', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post']

    def validate(self, attrs):
        user = attrs.get("user")
        post = attrs.get("post")

        if not user:
            raise serializers.ValidationError({"user": "Required User"})
        if not post:
            raise serializers.ValidationError({"post": "Required Post ID"})

        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("Ja Curtiu isso")

        return attrs


class LikeDeleteSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    post = serializers.IntegerField()

    def validate_user(self, value):
        if not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Usuário não encontrado.")
        return value

    def validate_post(self, value):
        if not Posts.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Post não encontrado.")
        return value

    def validate(self, attrs):
        user = attrs.get("user")
        post = attrs.get("post")

        if not Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("Like não encontrado para esse usuário e post.")

        return attrs
