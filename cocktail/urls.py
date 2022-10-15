from django.urls import path, include
from django.contrib import admin
from cocktail.views import CocktailAPIView, CocktailDetailAPIView, CategoryAPIView, CategoryDetailAPIView, IngredientAPIView, IngredientDetailAPIView
urlpatterns = [
    path('', CocktailAPIView.as_view()),
    path('<int:pk>/', CocktailDetailAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('ingredient/', IngredientAPIView.as_view()),
    path('ingredient/<int:pk>/', IngredientDetailAPIView.as_view()),
    
]
