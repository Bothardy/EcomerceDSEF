from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.all()

    return render(request, 'store/home.html', {'product': product})
