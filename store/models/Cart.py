from django.db import models
from .Client import  Customer
from .Product import  Product
class Cart(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='Cartitem')

    def __str__(self):
        return f"Cart for {self.client.fname}"
