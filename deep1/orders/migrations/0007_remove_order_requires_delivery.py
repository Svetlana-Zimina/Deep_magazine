# Generated by Django 4.2.11 on 2024-08-25 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_requires_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='requires_delivery',
        ),
    ]
