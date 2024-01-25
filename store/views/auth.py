from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models  import Product,Customer
from django.views import View




def auth(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)

    customer = Customer.objects.first()
    return render(request, 'store/auth.html', {'customer': customer})




