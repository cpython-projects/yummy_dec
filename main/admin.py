from django.contrib import admin
from .models import Category, Dish, Gallery, Event, ContactInfo, Reservation
from django.utils.safestring import mark_safe


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'price', 'category', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'category', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class DishInline(admin.StackedInline):
    model = Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        DishInline,
    ]


admin.site.register(Gallery)
admin.site.register(ContactInfo)
admin.site.register(Reservation)
