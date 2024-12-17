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


class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='url')
    short_desc = models.TextField(max_length=500, blank=True)
    desc = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='images/events/', blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('date_time',)
        unique_together = ['id', 'slug']
