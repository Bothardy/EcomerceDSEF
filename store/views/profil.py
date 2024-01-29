from django.shortcuts import render
from store.models import Product, Customer, CartItem, Order, Category
from django.shortcuts import render, get_object_or_404



def get_customer_profil(request):
    # Retrieve customer_id from the session, replace 'your_session_key' with the actual key you are using
    customer_id = request.session.get('Customer')

    # Get the selected customer or return a 404 response if not found
    customer = get_object_or_404(Customer, pk=customer_id)

    print("This customer is", customer)

    context = {
        'customer': customer,
    }

    return render(request, 'store/profil.html', context)