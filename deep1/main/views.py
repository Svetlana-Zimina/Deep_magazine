from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Бездна - Главная',
        'content': 'Журнал Ассоциации спелеологов Урала',
        'categories': categories
    }
    return render(request, 'main/index.html', context)
