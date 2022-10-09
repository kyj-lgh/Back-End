from rest_framework import serializers
from cocktail.models import Cocktail, Category, Ingredient

class CocktailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
    ingredient = serializers.SlugRelatedField(slug_field='name', many=True, queryset = Ingredient.objects.all())
    class Meta:
        model = Cocktail 
        fields = ['id', 'category', 'name', 'alcohol', 'ingredient', 'image', 'create_dt', 'bookmark']
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class IngerdientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']
        
        
# class CocktailCreateSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
#     ingredient = serializers.SlugRelatedField(slug_field='name', many=True, queryset = Ingredient.objects.all())
#     class Meta:
#         model = Cocktail
#         fileds='__all__'
#         exclude= ['update_dt']