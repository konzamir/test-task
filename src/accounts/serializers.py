from rest_framework import serializers
from accounts.models import UserModel as User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'],
            validated_data['password'])

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentionals!")
