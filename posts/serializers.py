from rest_framework import serializers
from account.serializers import UserListSerializer
from posts.models import Post, Category
from account.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True) 
    class Meta:
        model=Post
        fields = ['id', 'author', 'post_category', 'title', 'content', 'create_dt']

class PostCreateSerializer(serializers.ModelSerializer):
    post_category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
    class Meta:
        model=Post
        fields=['post_category', 'title', 'content']