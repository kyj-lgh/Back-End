from django.contrib.auth import get_user_model
from django.db import models
from account.models import User

class Cocktail(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  #칵테일 도수 카테고리, None부터 범위로 표시할 예정
    name = models.CharField('Cocktail_name', max_length=50, unique=True)
    alcohol = models.DecimalField('Alcohol', decimal_places=1, max_digits=100 ,null=True)   #정확한 도수 표시, 숫자만 쓰기 위해서 DecimalField 사용
    ingredient = models.ManyToManyField('Ingredient')   #재료 선택
    image = models.ImageField('IMAGE', upload_to='cocktail/%Y/%m/', blank=True, null=True)
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    bookmark = models.ManyToManyField(User) #즐겨찾기 기능

    class Meta:
        ordering = ('update_dt',)

    def __str__(self):
        return self.name

#유저 게시글, 자신만의 레시피 표현
class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    class Meta:
        ordering = ('update_dt',)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content
    

#칵테일에 들어가는 재료
class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name