from django.shortcuts import redirect, render

from goods.models import Products
from carts.models import Cart


def cart_add(request, product_slug):
    """Добавление товара в корзину."""

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(
            user=request.user,
            product=product
        )

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                user=request.user,
                product=product,
                quantity=1
            )

    return redirect(request.META.get('HTTP_REFERER'))


def cart_change(request, product_slug):
    """Изменение количества товара в корзине."""
    pass


def cart_remove(request, product_slug):
    """Удаление товара из корзины."""
    pass
