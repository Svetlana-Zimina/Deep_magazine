from django.urls import path

from carts import views


app_name = 'carts'

urlpatterns = [
    path('cart-add/', views.cart_add, name='cart-add'),
    path(
        'cart-change/',
        views.cart_change,
        name='cart-change'
    ),
    path(
        'cart-remove/',
        views.cart_remove,
        name='cart-remove'
    ),
]
