from django.db import models
from django.utils import timezone

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # string representation of the product
    def __str__(self):
        return self.name
        
    

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()

    def __str__(self):
        return f"{self.user_id} - {self.user_name}"