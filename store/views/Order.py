from django.shortcuts import render, redirect
from store.models.Cart import Order, CartItem
from django.shortcuts import render, get_object_or_404
def place_order(request):
    # Assuming you have a logged-in user and you store the customer ID in the session
    customer_id = request.session.get('Customer')

    # Fetch the cart items for the current customer
    cart_items = CartItem.objects.filter(cart__client_id=customer_id)


    # Create a new order for the customer
    order = Order.objects.create(customer_id=customer_id)

    # Associate cart items with the order
    for cart_item in cart_items:
        cart_item.order = order
        cart_item.save()

    # Optionally, you can clear the cart after placing the order
    # cart_items.delete()

    # Redirect to a page showing the order details or a thank you page
    return redirect('http://127.0.0.1:8000/show_cart/')

# views.py



# views.py



def order_detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order_items = CartItem.objects.filter(cart__client=order.customer)

    except Order.DoesNotExist:
        print(f"Order with ID {order_id} does not exist.")
        return render(request, 'store/OrderDetail.html')

    print("Order ID:", order.id)
    print("Customer ID:", order.customer.id)


    context = {
        'order': order,
        'order_items': order_items,

    }

    return render(request, 'store/OrderDetail.html', context)

