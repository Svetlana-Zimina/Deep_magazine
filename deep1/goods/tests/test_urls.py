from http import HTTPStatus

from django.test import Client, TestCase

from goods.models import Categories, Products


class GoodsURLTests(TestCase):

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
    
    def test_goods_urls_exist_at_desired_location(self): 
        """Проверка доступности адресов приложения goods."""

        url_status_code = { 
            '/catalog/all/': HTTPStatus.OK, 
            f'/catalog/{self.category.slug}/': HTTPStatus.OK, 
            f'/catalog/product/{self.product.slug}/': HTTPStatus.OK,
        } 

        for url, status_code in url_status_code.items(): 
            with self.subTest(url=url): 
                response = self.guest_client.get(url) 
                self.assertEqual(response.status_code, status_code)
    
    def test_goods_urls_uses_correct_templates(self): 
        """Проверка шаблонов приложения goods.""" 

        url_template = { 
            f'/catalog/{self.category.slug}/': 'goods/catalog.html', 
            f'/catalog/product/{self.product.slug}/': 'goods/product.html', 
        } 

        for url, template in url_template.items(): 
            with self.subTest(url=url): 
                response = self.guest_client.get(url) 
                self.assertTemplateUsed(response, template)
