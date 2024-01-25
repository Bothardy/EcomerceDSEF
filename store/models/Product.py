from django.db import models
from .Category import Category


class Product(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    description= models.TextField(max_length=25000, default='', blank=True, null= True)
    image= models.ImageField(upload_to='static/website/')
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

