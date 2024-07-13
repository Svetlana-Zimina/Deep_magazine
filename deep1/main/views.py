from typing import Any

# from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Главная'
        return context


class PaymentDeliveryView(TemplateView):
    template_name = 'main/payment_delivery.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Оплата и доставка'
        return context


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Контакты'
        return context


class WorkGroupView(TemplateView):
    template_name = 'main/work_group.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Над журналом работают'
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'main/privacy_policy.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Политика конфиденциальности'
        return context


# def index(request):

#     context = {
#         'title': 'Бездна - Главная',
#     }
#     return render(request, 'main/index.html', context)


# def payment_delivery(request):

#     context = {
#         'title': 'Бездна - Оплата и доставка',
#     }
#     return render(request, 'main/payment_delivery.html', context)


# def contacts(request):

#     context = {
#         'title': 'Бездна - Контакты',
#     }
#     return render(request, 'main/contacts.html', context)


# def work_group(request):

#     context = {
#         'title': 'Бездна - Над журналом работают',
#     }
#     return render(request, 'main/work_group.html', context)

# def privacy_policy(request):

#     context = {
#         'title': 'политика конфиденциальности',
#     }
#     return render(request, 'main/privacy_policy.html', context)

