from django.urls import path, include
from account.views import UserCreateAPIView, LoginAPIView
urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
