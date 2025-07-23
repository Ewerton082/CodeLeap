from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id']

    def validate_username(self, value):

        if self.instance:
            if User.objects.exclude(pk=self.instance.pk).filter(username=value).exists():
                raise serializers.ValidationError("This username is already in use.")
        else:
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("This username is already in use.")
        return value
