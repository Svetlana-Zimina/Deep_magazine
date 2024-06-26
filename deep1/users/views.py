# from django.shortcuts import render
from typing import Any
from django.views.generic import TemplateView


class UsersCartView(TemplateView):
    template_name = 'users/users-cart.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Корзина'
        return context


# def users_cart(request):
#     context = {
#         'title': 'Бездна - Корзина',
#     }
#     return render(request, 'users/users-cart.html', context)
