# Generated by Django 4.2.11 on 2024-04-03 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['id'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
