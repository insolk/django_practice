from django.db import models
from django.utils import timezone


class Product(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):

        return self.name
