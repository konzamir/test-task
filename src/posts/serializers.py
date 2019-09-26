from rest_framework import serializers

from .models import PostModel, CommendsModel, FilesModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = (
            'id', 'name', 'description', 'pub_time', 'user'
        )


class CommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommendsModel
        fields = (
            'text', 'user', 'post', 'parent', 'id'
        )


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = (
            'file', 'name', 'post'
        )
