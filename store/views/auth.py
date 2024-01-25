from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.Product import Products
from django.views import View


def auth(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)

    return render(request, 'store/auth.html')