from rest_framework import viewsets
from account.models import User
from posts.models import Post
from posts.permissions import CustomReadOnly
from posts.serializers import PostSerializer, PostCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (CustomReadOnly, )
    
    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
