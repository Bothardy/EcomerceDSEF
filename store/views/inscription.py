from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.Client import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'store/inscription.html')

    def post(self, request):
        postData = request.POST

        email = postData.get('email')
        username = postData.get('username')
        password = postData.get('password')
        # validation
        value = {

            'username': username,
            'email': email,
            'password': password
        }
        error_message = None

        customer = Customer(username=username,
                            email=email,
                            password=password)
        error_message = False

        if not error_message:
            print(username, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'inscription.html', data)

        return error_message
