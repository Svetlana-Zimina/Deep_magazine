# Generated by Django 4.2.11 on 2024-07-05 16:32

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0008_products_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('user_first_name', models.CharField(max_length=100, verbose_name='Имя покупателя')),
                ('user_last_name', models.CharField(max_length=100, verbose_name='Фамилия покупателя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=100, verbose_name='Электронная почта')),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Требуется доставка')),
                ('delivery_type', models.CharField(blank=True, choices=[('Яндекс доставка', 'Яндекс доставка'), ('Почта', 'Почта')], max_length=250, null=True, verbose_name='Способ доставки')),
                ('pickup_place', models.CharField(blank=True, choices=[('«Посольство Уральских гор»', '«Посольство Уральских гор»'), ('«Территория странствий»', '«Территория странствий»'), ('«Центр путешественников»', '«Центр путешественников»'), ('Клуб СГС', 'Клуб СГС'), ('Магазин SportX', 'Магазин SportX'), ('Пермский спелеоклуб', 'Пермский спелеоклуб'), ('«Земля приключений»', '«Земля приключений»'), ('«Вертикаль»', '«Вертикаль»'), ('«Геккон»', '«Геккон»')], max_length=250, null=True, verbose_name='Пункт самовывоза')),
                ('delivery_address', models.TextField(blank=True, null=True, verbose_name='Адрес доставки')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.CharField(choices=[('В обработке', 'В обработке'), ('На доставке', 'На доставке'), ('Завершен', 'Завершен')], default='В обработке', max_length=50, verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
                'db_table': 'order_item',
            },
        ),
    ]
