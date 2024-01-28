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
        cart_item.quantity = 0
        cart_item.quantity += 1
        cart_item.save()

        messages.success(request, 'Successfully added item to your cart!')

        return redirect('home.html')
    else:
        # Handle the case where the customer is not authenticated (redirect to login page or show a message)
        return redirect('login.html')  # Adjust this to your login view name or provide a custom message


def show_cart(request):
    # Assuming you have a logged-in user and you store the customer ID in the session
    customer_id = request.session.get('Customer')
    param_value = request.GET.get('viewcart', None)

    # Fetch the cart items for the current customer
    cart_items = CartItem.objects.filter(cart__client_id=customer_id)

    # Calculate total quantity and subtotal
    total_quantity = sum(item.quantity for item in cart_items)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    # Debugging information Testin BBLCOK
    print("Customer ID:", customer_id)
    print("Cart Items:", cart_items)
    print("Total Quantity:", total_quantity)
    print("Subtotal:", subtotal)
# END TESTING BLOCK
    context = {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'subtotal': subtotal,
        'param_value': param_value,
    }

    return render(request, 'store/Cart.html', context)

