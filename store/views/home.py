from django.shortcuts import render
from store.models import Product, Customer

def get_products():
    # Fetch all products from the database
    return Product.objects.all()

def get_customer_name(request):
    # Retrieve the customer ID from the session
    customer_id = request.session.get('Customer')

    # Fetch the customer object if the ID exists
    customer = None
    if customer_id:
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # Handle the case where the customer does not exist
            pass

    return customer.fname if customer else None

def home(request):
    # Get products and customer name
    product = get_products()
    customer_name = get_customer_name(request)

    # Pass the customer's name and products to the template
    context = {'product': product, 'customer_name': customer_name}
    return render(request, 'store/home.html', context)
