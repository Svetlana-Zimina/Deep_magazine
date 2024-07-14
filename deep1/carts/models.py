from django.db import models

from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    """Класс для получения суммы и количества товаров в корзине."""

    def total_price(self):
        """Полная сумма товаров в корзине."""

        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """Полное количество товаров в корзине."""

        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Cart(models.Model):
    """Модель Корзина."""

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='carts'
    )
    product = models.ForeignKey(
        Products,
        verbose_name='Продукт',
        on_delete=models.CASCADE,
        related_name='carts'
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    session_key = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='Ключ сессии'
    )

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = CartQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.first_name} {self.user.last_name} | Товар {self.product.name} | Количество {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'

    def products_price(self):
        """Метод считает общую стоимость определенного продукта в корзине."""

        return round(self.product.sell_price() * self.quantity, 2)
