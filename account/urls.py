from django.urls import path, include
from account.views import UserCreateAPIView, LoginAPIView, UserListAPIView, UserRetrieveUpdateView
urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('current', UserRetrieveUpdateView.as_view()),
    path('user/', UserListAPIView.as_view()),
]
