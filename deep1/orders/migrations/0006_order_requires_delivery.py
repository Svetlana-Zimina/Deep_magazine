# Generated by Django 4.2.11 on 2024-08-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_requires_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='requires_delivery',
            field=models.BooleanField(default=False, verbose_name='Требуется доставка'),
        ),
    ]
