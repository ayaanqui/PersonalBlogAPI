from django.utils.text import Truncator
from rest_framework import serializers
from posts.models import Post
from tags.models import Tag
from tags.api.serializers import TagSerializer


class PostSummarySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    summary = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'summary',
            'published',
            'tags',
            'views'
        ]

    def get_summary(self, obj):
        return Truncator(obj.content).words(25, html=True)


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'