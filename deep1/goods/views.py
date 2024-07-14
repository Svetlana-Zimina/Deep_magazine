import os
from typing import Any

# from django.core.paginator import Paginator
# from django.db.models import QuerySet
from django.db.models.base import Model as Model
# from django.shortcuts import get_list_or_404
from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView

from goods.models import Products


class CatalogView(ListView):
    """Представление для модели Каталог."""

    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        """Получение списка объектов для отображения."""

        category_slug = self.kwargs.get('category_slug')
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')

        if category_slug == 'all':
            goods = super().get_queryset()
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != 'default':
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        """Заполнение словаря контекста категории."""

        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - каталог'
        context['slug_url'] = self.kwargs.get('category_slug')
        return context


class ProductView(DetailView):
    """представление для модели Продукты."""

    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_object(self, queryset=None) -> Model:
        """Получение продукта по слагу."""

        product = Products.objects.get(
            slug=self.kwargs.get(self.slug_url_kwarg)
        )
        return product

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Заполнение словаря контекста продукта."""

        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class FileDownloadView(View):
    """Представление для скачивания файла с сайта."""

    content_type_value = 'text/plain'
    slug_url_kwarg = 'product_slug'

    def get(self, request):
        product = Products.objects.get(
            slug=self.kwargs.get(self.slug_url_kwarg)
        )
        file_name = f'{product.name}.pdf'

        file_path = os.path.join(self.folder_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(
                    f.read(),
                    content_type=self.content_type_value
                )
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        else:
            raise Http404


# def catalog(request, category_slug):

#     page = request.GET.get('page', 1)

#     on_sale = request.GET.get('on_sale', None)
#     order_by = request.GET.get('order_by', None)

#     if category_slug == 'all':
#         goods = Products.objects.all()
#     else:
#         goods = get_list_or_404(
#             Products.objects.filter(category__slug=category_slug)
#         )

#     if on_sale:
#         goods = goods.filter(discount__gt=0)

#     if order_by and order_by != 'default':
#         goods = goods.order_by(order_by)

#     paginator = Paginator(goods, 6)
#     current_page = paginator.page(int(page))

#     context = {
#         'title': 'Бездна - каталог',
#         'goods': current_page,
#         'slug_url': category_slug
#     }
#     return render(request, 'goods/catalog.html', context)


# def product(request, product_slug):

#     product = Products.objects.get(slug=product_slug)

#     context = {
#         'product': product
#     }

#     return render(request, 'goods/product.html', context=context)
