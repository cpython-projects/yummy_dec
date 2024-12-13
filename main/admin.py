from django.contrib import admin
from .models import Category, Dish, Gallery


# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Gallery)
