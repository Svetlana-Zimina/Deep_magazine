from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from goods.models import Products

# from users.models import User


DELIVERY_TYPES = (
    ('Яндекс доставка', 'Яндекс доставка'),
    ('Почта', 'Почта'),
)

PICKUP_PLACES = (
    ('«Посольство Уральских гор»', '«Посольство Уральских гор»'),
    ('«Территория странствий»', '«Территория странствий»'),
    ('«Центр путешественников»', '«Центр путешественников»'),
    ('Клуб СГС', 'Клуб СГС'),
    ('Магазин SportX', 'Магазин SportX'),
    ('Пермский спелеоклуб', 'Пермский спелеоклуб'),
    ('«Земля приключений»', '«Земля приключений»'),
    ('«Вертикаль»', '«Вертикаль»'),
    ('«Геккон»', '«Геккон»')
)

STATUS_LIST = (
    ('В обработке', 'В обработке'),
    ('На доставке', 'На доставке'),
    ('Завершен', 'Завершен'),
)


class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        """Полная сумма товаров в заказе."""

        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """Полное количество товаров в заказе."""

        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Order(models.Model):
    """Модель Заказы."""

    # user = models.ForeignKey(
    #     User,
    #     verbose_name='Пользователь',
    #     on_delete=models.SET_DEFAULT,
    #     default=None,
    #     related_name='orders',
    #     blank=True,
    #     null=True
    # )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа'
    )
    user_first_name = models.CharField(
        max_length=100,
        verbose_name='Имя покупателя',
    )
    user_last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия покупателя',
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона',
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Электронная почта'
    )
    # requires_delivery = models.BooleanField(
    #     default=False,
    #     verbose_name='Требуется доставка'
    # )
    delivery_type = models.CharField(
        max_length=250,
        verbose_name='Способ доставки',
        null=True,
        blank=True,
        choices=DELIVERY_TYPES
    )
    pickup_place = models.CharField(
        max_length=250,
        verbose_name='Пункт самовывоза',
        null=True,
        blank=True,
        choices=PICKUP_PLACES
    )
    delivery_address = models.TextField(
        null=True,
        blank=True,
        verbose_name='Адрес доставки'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Оплачено'
    )
    status = models.CharField(
        max_length=50,
        default='В обработке',
        verbose_name='Статус заказа',
        choices=STATUS_LIST
    )
    send_to_email = models.BooleanField(
        default=False,
        verbose_name='Выслать на электронную почту'
    )

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.pk} | Покупатель {self.user_first_name} {self.user_last_name}'


class OrderItem(models.Model):
    """Промежуточная модель Заказ-Продукт."""

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name='Продукт',
        null=True
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена'
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата продажи'
    )

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    objects = OrderitemQueryset.as_manager

    def products_price(self):
        """Получение цены продукта."""

        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f'Товар {self.product} | Заказ № {self.order.pk}'
