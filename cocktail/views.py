from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView

from cocktail.models import Cocktail, Category, Ingredient
from cocktail.serializers import CategorySerializer, CocktailSerializer, IngredientSerializer

class CocktailAPIView(ListCreateAPIView):   #칵테일 리스트, 생성 API
    permission_classes=(AllowAny,)
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer  

class CocktailDetailAPIView(RetrieveUpdateDestroyAPIView):      #수정, 삭제 API
    permission_classes=(AllowAny,)
    serializer_class = CocktailSerializer
    
    def get_queryset(self):
        return Cocktail.objects.filter(pk = self.kwargs["pk"])     #kwargs = pk 전달 용도
    
class CategoryAPIView(ListCreateAPIView):
    permission_classes=(AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.filter(pk = self.kwargs["pk"])     #kwargs = pk 전달 용도
    
    
class IngredientAPIView(ListCreateAPIView):
    permission_classes=(AllowAny, )
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class IngredientDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = IngredientSerializer
    
    def get_queryset(self):
        return Ingredient.objects.filter(pk = self.kwargs["pk"])     #kwargs = pk 전달 용도