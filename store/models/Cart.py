from django.db import models
from .Client import Customer
from .Product import Product


class Cart(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.client.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    livraisonStatus=models.CharField(blank=True,max_length=50,default="encours")

    def __str__(self):
        return f"Order for {self.customer.username}"



