from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
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
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.owner_name


class Client(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(default='qwert@gmai.com', null=True)
    bucket = models.ForeignKey(Bucket, on_delete=CASCADE)

    def __str__(self):
        return self.user_name


class City(models.Model):
    city_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    client = models.ManyToManyField(Client)

    def __str__(self):
        return self.city_name
