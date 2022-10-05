from django.urls import path, include
from django.contrib import admin
from cocktail.views import CocktailCreateAPIView, CocktailListAPIView
urlpatterns = [
    path('account/', include('account.urls')),
    path('cocktail/', CocktailListAPIView.as_view()),
    path('create-cocktail/', CocktailCreateAPIView.as_view()),
]
