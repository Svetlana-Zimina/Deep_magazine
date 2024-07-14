from django.test import Client, TestCase
from django.urls import reverse

from goods.models import Categories, Products


class GoodsViewstests(TestCase):
    """Тестирование представлений приложения goods."""

    @classmethod
    def setUpClass(cls):
        """Создание тестовых данных."""

        super().setUpClass()
        cls.guest_client = Client()

        cls.category = Categories.objects.create(
            name='Категория 1',
            slug='category1'
        )
        cls.product = Products.objects.create(
            name='Продукт 1',
            slug='product1',
            category=cls.category,
            price=10,
            discount=0,
            quantity=1,
        )

    def test_pages_uses_correct_template(self):
        """URL-адрес приложения goods использует соответствующий шаблон."""

        templates_pages_names = {
            'goods/catalog.html': reverse(
                'catalog:index',
                kwargs={'slug': f'{self.category.slug}'}
            ),
            'goods/product.html': reverse(
                'catalog:product',
                kwargs={'slug': f'{self.product.slug}'}
            ),
        }

        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
