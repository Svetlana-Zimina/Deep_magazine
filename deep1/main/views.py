from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Бездна - Главная',
        'content': 'Журнал Ассоциации спелеологов Урала'
    }
    return render(request, 'main/index.html', context)
