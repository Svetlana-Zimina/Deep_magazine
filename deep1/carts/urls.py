from django.urls import path

from carts import views


app_name = 'carts'

urlpatterns = [
    path('cart-add/', views.CartAddView.as_view(), name='cart-add'),
    path(
        'cart-change/',
        views.CartChangeView.as_view(),
        name='cart-change'
    ),
    path(
        'cart-remove/',
        views.CartRemoveView.as_view(),
        name='cart-remove'
    ),
]
