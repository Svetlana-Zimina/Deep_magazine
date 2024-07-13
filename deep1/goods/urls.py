from django.urls import path, re_path
from django.views.static import serve

from deep import settings
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='index'),
    path(
        'product/<slug:product_slug>/',
        views.ProductView.as_view(),
        name='product'
    ),
    re_path(
        r"^download/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT}
    ),
]
