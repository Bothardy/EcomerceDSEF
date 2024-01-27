from django.contrib import admin
from store.models import Product, Category, Customer, CartItem, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Cart)
