from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Страница в разработке'
    }
    return render(request, 'main/index.html', context)
