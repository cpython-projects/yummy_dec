from django.contrib import admin
from .models import Category, Dish, Gallery, Event


# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Event)
