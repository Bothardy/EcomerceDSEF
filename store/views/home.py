from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.Product import Product
from django.views import View


# Create your views here.

def home(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.first()

    return render(request, 'store/home.html', {'product': product})

