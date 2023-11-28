from django.shortcuts import render, redirect
from .models import Category, User
from .forms import UserForm, ClientForm, AuthUserForm, ResponseForm


def categories(request):
    """
    View function to display a list of product categories.

    Retrieves all categories from the database and renders them in the 'main/categories.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the list of categories.
    """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'main/categories.html', context)


def create_user(request):
    """
    View function to handle the creation of User instances.

    If the request method is POST, validates the UserForm and saves the form data to the database.
    If the request method is GET, initializes a new UserForm for user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the form for creating a new user.
    """

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def create_client(request):
    """
    View function to handle the creation of Client instances.

    If the request method is POST, validates the ClientForm and saves the form data to the database.
    If the request method is GET, initializes a new ClientForm for user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the form for creating a new client.
    """

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def auth(request):
    """
    View function to handle user authentication.

    If the request method is POST, validates the AuthUserForm, checks for user existence,
    and redirects to the appropriate page.
    If the request method is GET, initializes a new AuthUserForm for user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the form for user authentication.
    """

    if request.method == "POST":
        form = AuthUserForm(request.POST)
        if form.is_valid():
            user_exists = User.objects.filter(login=form.cleaned_data['login'],
                                              password1=form.cleaned_data['password1']).exists()
            if user_exists:
                return redirect('categories')
            else:
                return redirect('login')
    else:
        form = AuthUserForm()

    context = {
        'form': form
    }
    return render(request, 'main/auth.html', context)


def response_get(request):
    """
    View function to handle the creation of Response instances.

    If the request method is POST, validates the ResponseForm and saves the form data to the database.
    If the request method is GET, initializes a new ResponseForm for user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the form for creating a new response.
    """

    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ResponseForm()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
