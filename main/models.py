from django.db import models
from django.db.models import CASCADE

# Create your models here.

class Category(models.Model):
    """
    Represents a product category.

    Attributes:
    - category_name (str): The name of the category.
    """

    category_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Represents a product.

    Attributes:
    - product_name (str): The name of the product.
    - price (int): The price of the product.
    - description (str): A brief description of the product.
    - discount (int): The discount percentage applied to the product.
    - category (Category): The category to which the product belongs.
    - country (str): The country of origin for the product.
    - firm (str): The manufacturing firm of the product.
    """

    product_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    country = models.CharField(max_length=255, default=0)
    firm = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Bucket(models.Model):
    """
    Represents a user's shopping bucket.

    Attributes:
    - owner_name (str): The name of the bucket owner.
    - products (ManyToManyField): The products added to the bucket.
    """

    owner_name = models.CharField(max_length=255, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.owner_name


class Client(models.Model):
    """
    Represents a client/user.

    Attributes:
    - user_name (str): The username of the client.
    - name (str): The name of the client.
    - email (str): The email address of the client.
    - bucket (Bucket): The shopping bucket associated with the client.
    """

    user_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(default='qwert@gmai.com', null=True)
    bucket = models.ForeignKey(Bucket, on_delete=CASCADE)

    def __str__(self):
        return self.user_name


class City(models.Model):
    """
    Represents a city.

    Attributes:
    - city_name (str): The name of the city.
    - country (str): The country in which the city is located.
    - client (ManyToManyField): The clients associated with the city.
    """

    city_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    client = models.ManyToManyField(Client)

    def __str__(self):
        return self.city_name


class User(models.Model):
    """
    Model representing a user.

    Attributes:
        name (CharField): The user's name.
        surname (CharField): The user's surname.
        login (CharField): The user's login.
        password1 (CharField): The user's password.
        password2 (CharField): A second field for the user's password (confirmation).
        country (CharField): The user's country.
        email (EmailField): The user's email address.
        phone (IntegerField): The user's phone number.
    """

    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    login = models.CharField(max_length=255, null=True, blank=True)
    password1 = models.CharField(max_length=255, null=True, blank=True)
    password2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(default='qwert@gmai.com', null=True)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: The user's name.
        """

        return self.name


class Response(models.Model):
    """
    Model representing a user response.

    Attributes:
        EVALUATION_CHOICES (list): Choices for response evaluations.
        REACTIONS (list): Choices for user reactions.
        products (ManyToManyField): Relationship with Product model.
        img (ImageField): Image associated with the response.
        email (EmailField): The user's email address.
        choice_evaluations (IntegerField): The chosen evaluation from EVALUATION_CHOICES.
        reaction (IntegerField): The chosen reaction from REACTIONS.
        phone (IntegerField): The user's phone number.
    """

    EVALUATION_CHOICES = [
        (1, 'Дуже погано'),
        (2, 'Погано'),
        (3, 'Задовільно'),
        (4, 'Добре'),
        (5, 'Відміно'),
    ]

    REACTIONS = [
        (1, 'Негативний відгук'),
        (2, 'Позитивний відгук')
    ]

    products = models.ManyToManyField(Product)
    img = models.ImageField(null=True, blank=True)
    email = models.EmailField(default='qwert@gmai.com', null=True)
    choice_evaluations = models.IntegerField(default=0, choices=EVALUATION_CHOICES)
    reaction = models.IntegerField(default=0, choices=REACTIONS)
    phone = models.IntegerField(null=True, blank=True)
