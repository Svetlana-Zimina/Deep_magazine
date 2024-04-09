from django.shortcuts import render


def users_cart(request):
    return render(request, 'users/users-cart.html')
