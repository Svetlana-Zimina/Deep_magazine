from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """Модель Категория."""

    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    """Модель Продукты."""

    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='goods_images',
        blank=True,
        null=True
    )
    image_2 = models.ImageField(
        verbose_name='Изображение 2',
        upload_to='goods_images',
        blank=True,
        null=True
    )
    image_3 = models.ImageField(
        verbose_name='Изображение 3',
        upload_to='goods_images',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name='Цена',
        default=0.00,
        max_digits=7,
        decimal_places=2
    )
    discount = models.DecimalField(
        verbose_name='Скидка в процентах',
        default=0.00,
        max_digits=4,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0
    )
    category = models.ForeignKey(
        Categories,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='products'
    )
    pdf_file = models.FileField(
        verbose_name='Файл PDF',
        upload_to='pdf_files',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['id', ]
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Формирование нужного URL-адреса по слагу."""

        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        """Отображение id товара на сайте."""

        return f'{self.id:05}'

    def sell_price(self):
        """Расчет стоимости товара с учетом скидки."""

        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
