from django.db import models


class Categories(models.Model):
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

    class Meta:
        ordering = ['id',]
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)

        return self.price
