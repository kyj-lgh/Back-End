from django.urls import path
from rest_framework import routers
from posts.views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
