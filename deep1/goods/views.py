from typing import Any
# from django.core.paginator import Paginator
# from django.db.models import QuerySet
from django.db.models.base import Model as Model
# from django.shortcuts import get_list_or_404
from django.views.generic import DetailView, ListView

from goods.models import Products


class CatalogView(ListView):
    
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - каталог'
        context['slug_url'] = self.kwargs.get('category_slug')
        return context


class ProductView(DetailView):

    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    
    def get_object(self, queryset=None) -> Model:
        product = Products.objects.get(
            slug=self.kwargs.get(self.slug_url_kwarg)
        )
        return product
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


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
