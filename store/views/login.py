from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models  import Product,Customer
from django.views import View
from django.contrib.auth.hashers import  check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import HttpResponse
class Login(View):
    return_url = None


    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'store/login.html')


    def post(self,request):
        # Fetch the first product from the database (you can modify this logic based on your needs)

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer = Customer.get_customer_by_email(email)
            error_message = None
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['Customer'] = customer.id

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('home.html')
                else:
                    error_message = 'Invalid !password!'
            else:
                error_message = 'Invalid !email !'

            print(email, password)
            return render(request, 'store/login.html', {'error': error_message})




