from django.urls import path, include
from account.views import UserCreateAPIView, LoginAPIView, UserListAPIView, UserRetrieveUpdateView
urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
    path('user/edit/', UserRetrieveUpdateView.as_view()),
    path('user/list/', UserListAPIView.as_view()),
]
