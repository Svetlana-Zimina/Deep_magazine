# Generated by Django 4.2.11 on 2024-08-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_send_to_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='requires_delivery',
        ),
    ]
