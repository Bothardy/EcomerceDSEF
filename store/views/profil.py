from django.shortcuts import render
from store.models import Product, Customer, CartItem, Order, Category
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.Client import Customer
from django.views import View

class updatec(View):
    def get(self, request):
        return render(request, 'store/profil.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get('fname')
        adresse = postData.get('adresse')
        phone = postData.get('phone')
        email = postData.get('email')
        username = postData.get('username')
        password = postData.get('password')

        # Retrieve the existing customer if available
        customer_id = request.session.get('Customer')
        if customer_id:
            customer = Customer.objects.get(pk=customer_id)
        else:
            # Handle the case where customer doesn't exist
            customer = Customer()

        # Update customer fields
        customer.fname = fname
        customer.adresse = adresse
        customer.phone = phone
        customer.email = email
        customer.username = username
        customer.password = make_password(password)

        # Save the customer
        customer.save()

        # Redirect to the login page upon successful update
        return redirect('login.html')


def get_customer_profil(request):
    # Retrieve customer_id from the session, replace 'your_session_key' with the actual key you are using
    customer_id = request.session.get('Customer')

    # Get the selected customer or return a 404 response if not found
    customer = get_object_or_404(Customer, pk=customer_id)

    print("This customer is", customer.email)

    context = {
        'customer': customer,
        'fname': customer.fname,

        # You can add more attributes here if needed

    }

    return render(request, 'store/profil.html', context)