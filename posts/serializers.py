from rest_framework import serializers
from account.serializers import UserListSerializer
from posts.models import Post, Comment
from account.models import User
from cocktail.models import Category

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','author', 'content']
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content']
        


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True) 
    post_category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
    class Meta:
        model=Post
        fields = ['id', 'author', 'post_category', 'title', 'content', 'create_dt', 'comments']

class PostCreateSerializer(serializers.ModelSerializer):
    post_category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
    class Meta:
        model=Post
        fields=['post_category', 'title', 'content']
        
