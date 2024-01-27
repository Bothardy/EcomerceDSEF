from django.contrib import admin
from store.models import Product, Category, Customer , Cart
from store.models.Cart import  CartItem,Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(Order)
