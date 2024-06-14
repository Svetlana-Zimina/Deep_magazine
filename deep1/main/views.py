from django.shortcuts import render


def index(request):

    context = {
        'title': 'Бездна - Главная',
    }
    return render(request, 'main/index.html', context)


def payment_delivery(request):

    context = {
        'title': 'Бездна - Оплата и доставка',
    }
    return render(request, 'main/payment_delivery.html', context)


def contacts(request):

    context = {
        'title': 'Бездна - Контакты',
    }
    return render(request, 'main/contacts.html', context)


def work_group(request):

    context = {
        'title': 'Бездна - Над журналом работают',
    }
    return render(request, 'main/work_group.html', context)

def privacy_policy(request):

    context = {
        'title': 'политика конфиденциальности',
    }
    return render(request, 'main/privacy_policy.html', context)

