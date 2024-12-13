from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/dishes/')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/gallery/')
    is_visible = models.BooleanField(default=True)

    sort = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



