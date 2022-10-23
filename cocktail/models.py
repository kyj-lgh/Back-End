from django.contrib.auth import get_user_model
from django.db import models
from account.models import User

class Cocktail(models.Model):
    cocktail_category = models.ForeignKey('Category', on_delete=models.CASCADE)  #칵테일 도수 카테고리, None부터 범위로 표시할 예정
    name = models.CharField('Cocktail_name', max_length=50, unique=True)
    alcohol = models.DecimalField('Alcohol', decimal_places=1, max_digits=100 ,null=True)   #정확한 도수 표시, 숫자만 쓰기 위해서 DecimalField 사용
    ingredient = models.ManyToManyField('Ingredient')   #재료 선택
    image = models.ImageField('IMAGE', upload_to='media/cocktail/', blank=True, null=True)
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    class Meta:
        ordering = ('update_dt',)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

#칵테일에 들어가는 재료
class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name