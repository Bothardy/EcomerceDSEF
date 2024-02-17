from django.urls import path, include
from store.views.login import Login
from store.views.inscription import Signup
from store.views.home import products_by_category ,  product_detail
from django.contrib.auth.views import LogoutView
from store.views.Cartview import add_to_cart, show_cart
from store.views.Order import place_order, order_detail
from store.views.Paypal import payment_checkout, create_payment, execute_payment, payment_failed
from store.views.profil import get_customer_profil,updatec

urlpatterns = [

    path('login', Login.as_view(), name='login.html'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('inscription', Signup.as_view(), name='inscription.html'),
    path('profil/', get_customer_profil, name='customer_profil'),
    path('update_profil', updatec.as_view(), name='update_profil'),

    # other URL patterns

    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),


    path('show_cart/', show_cart, name='show_cart'),
    path('place_order/', place_order, name='place_order'),

    # for flitering


    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('products/category/<int:category_id>/', products_by_category, name='products_by_category'),

    # for payement
    path('checkout/', payment_checkout, name='checkout_payment'),
    path('create_payment/', create_payment, name='create_payment'),
    path('execute_payment/', execute_payment, name='execute_payment'),
    path('payment_failed/', payment_failed, name='payment_failed'),

    path('product/<int:pk>/', product_detail, name='product_detail'),
]
