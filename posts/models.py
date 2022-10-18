from django.db import models
from cocktail.models import User, Category

#유저 게시글, 자신만의 레시피 표현
class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='author')
    post_category = models.ForeignKey('cocktail.Category', on_delete = models.CASCADE, null=True)
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    class Meta:
        ordering = ('update_dt',)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content

