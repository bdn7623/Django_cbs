from django.shortcuts import render
from .models import Category

# Create your views here.
def categories(request):
    """
    View function to display a list of product categories.

    Retrieves all categories from the database and renders them in the 'main/categories.html' template.

    Args:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML response containing the list of categories.
    """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'main/categories.html', context)
