# Generated by Django 4.2.11 on 2024-04-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_products_image_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files', verbose_name='Файл PDF'),
        ),
    ]
