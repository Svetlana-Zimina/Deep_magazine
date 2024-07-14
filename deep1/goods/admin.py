from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Настройки модели Категории
    для отображения в панели администратора."""

    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = ['name', ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Настройки модели Продукт
    для отображения в панели администратора."""

    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = [
        'name', 'quantity', 'price', 'discount'
    ]
    list_editable = [
        'discount',
    ]
    search_fields = [
        'name', 'descript'
    ]
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        'image_2',
        'image_3',
        'pdf_file',
        ('price', 'discount'),
        'quantity'
    ]
    list_filter = ['category', ]
