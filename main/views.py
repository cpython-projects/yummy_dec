from django.shortcuts import render
from .models import Category,Gallery


# Create your views here.
def home(request):
    # all, filter, get, first, last
    categories = Category.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)

    context = {
        'categories': categories,
        'gallery': gallery,
    }
    return render(request, 'menu.html', context=context)
