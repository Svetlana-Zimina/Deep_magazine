# Generated by Django 4.2.11 on 2024-08-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_order_requires_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='send_to_email',
            field=models.BooleanField(verbose_name='Выслать на электронную почту'),
        ),
    ]
