from django.shortcuts import render
from .models import Category, Gallery, Event
from django.db import models
from django.utils.timezone import now


# Create your views here.
def home(request):
    # all, filter, get, first, last
    categories = Category.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    events = Event.objects.filter(models.Q(date_time__isnull=True) | models.Q(date_time__gte=now())).filter(is_visible=True)

    context = {
        'categories': categories,
        'gallery': gallery,
        'events': events,
    }
    return render(request, 'main.html', context=context)
