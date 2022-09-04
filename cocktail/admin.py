from django.contrib import admin
from .models import *
from account.models import *

admin.site.register(Cocktail)
admin.site.register(Ingredient)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(User)