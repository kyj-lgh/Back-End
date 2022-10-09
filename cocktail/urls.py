from django.urls import path, include
from django.contrib import admin
from cocktail.views import CocktailAPIView, CocktaildetailAPIView
urlpatterns = [
    path('account/', include('account.urls')),
    path('', CocktailAPIView.as_view()),
    path('<int:pk>/', CocktaildetailAPIView.as_view()),
]
