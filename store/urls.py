

from django.urls import path, include
from store.views.login import Login
from store.views.inscription import Signup
from store.views.home import products_by_category
from django.contrib.auth.views import LogoutView
from store.views.Cartview import add_to_cart, show_cart
from store.views.Order import place_order, order_detail
urlpatterns = [

    path('login', Login.as_view(), name='login.html'),
    path('inscription', Signup.as_view(), name='inscription.html'),

    # other URL patterns

    path("logout/", LogoutView.as_view(), name="logout"),

    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path('show_cart/', show_cart, name='show_cart'),
    path('place_order/', place_order, name='place_order'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('products/category/<int:category_id>/', products_by_category, name='products_by_category'),

]
