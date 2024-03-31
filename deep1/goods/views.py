from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Бездна - каталог',
        'goods': [
            {'image': 'deps/images/goods/deep_43.jpg',
             'name': '"Бездна" №43',
             'description': 'Журнал "Бездна" №43, печатная версия',
             'price': 500.00},
            {'image': 'deps/images/goods/deep_43.jpg',
             'name': '"Бездна" №43 pdf',
             'description': 'Журнал "Бездна" №43, pdf формат',
             'price': 250.00},
            {'image': 'deps/images/goods/sticker_1.jpg',
             'name': 'Наклейки 1',
             'description': 'Наклейки "Спелеокотик" вриант 1',
             'price': 100.00},
            {'image': 'deps/images/goods/sticker_2.jpg',
             'name': 'Наклейки 2',
             'description': 'Наклейки "Спелеокотик" вриант 1',
             'price': 100.00},
            {'image': 'deps/images/goods/deep_46.jpg',
             'name': '"Бездна" №46',
             'description': 'Журнал "Бездна" №46, печатная версия',
             'price': 500.00},
            {'image': 'deps/images/goods/deep_46.jpg',
             'name': '"Бездна" №46 pdf',
             'description': 'Журнал "Бездна" №46, pdf формат',
             'price': 250.00}
        ]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
