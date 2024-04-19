from django.shortcuts import render


def users_cart(request):
    context = {
        'title': 'Бездна - Корзина',
    }
    return render(request, 'users/users-cart.html', context)
