from django.urls import path, include
from account.views import UserCreateAPIView
urlpatterns = [
    path('create/', UserCreateAPIView.as_view())
]
