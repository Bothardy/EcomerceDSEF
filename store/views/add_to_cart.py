# views.py
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, Cart, Customer
from store.models.Cart import CartItem
from django.contrib import messages
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the customer is authenticated
    if request.session.get('Customer'):
        customer_id = request.session.get('Customer')
        print(customer_id)
        # Check if the customer has an existing cart, create one if not
        user_cart, created = Cart.objects.get_or_create(client_id=customer_id)

        # Check if the product is already in the cart, create a new item or update the quantity
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        messages.success(request, 'Successfully added item to your cart!')

        return redirect('home.html')
    else:
        # Handle the case where the customer is not authenticated (redirect to login page or show a message)
        return redirect('login.html')  # Adjust this to your login view name or provide a custom message
