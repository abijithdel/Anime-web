from django.contrib import admin
from . models import Category,Content,animes,Movies
# Register your models here.

admin.site.register(Category)
admin.site.register(Content)
admin.site.register(animes)
admin.site.register(Movies)