from django.shortcuts import render
from store.models import Product, Customer, CartItem, Order, Category


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
    cart_item_count = CartItem.objects.filter(cart__client_id=request.session.get('Customer')).count()
    # get id of orders
    orders = Order.objects.all()

    # Pass the customer's name and products to the template
    context = {'product': product, 'customer_name': customer_name, 'cart_item_count': cart_item_count, 'orders': orders}
    return render(request, 'store/home.html', context)


def products_by_category(request, category_id):
    # Get the selected category
    category = Category.objects.get(pk=category_id)

    print("this categorie is ",category)

    # Get all products belonging to the selected category
    product = Product.objects.filter(category=category)

    context = {
        'category': category,
        'product': product,
    }

    return render(request, 'store/home.html', context)
