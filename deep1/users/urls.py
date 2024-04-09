from django.urls import path

from users import views


app_name = 'users'

urlpatterns = [
    path('users-cart/', views.users_cart, name='users-cart'),
]
