from django.shortcuts import render
from .models import *

# Create your views here.
def categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }


    return render(request, 'main/categories.html', context)
