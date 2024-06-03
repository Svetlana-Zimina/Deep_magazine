import shutil
import tempfile
from django.test import TestCase, Client, override_settings
from http import HTTPStatus
from django.core.files.uploadedfile import SimpleUploadedFile

from deep import settings
from goods.models import Categories, Products


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
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
        small_gif = (            
             b'\x47\x49\x46\x38\x39\x61\x02\x00'
             b'\x01\x00\x80\x00\x00\x00\x00\x00'
             b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
             b'\x00\x00\x00\x2C\x00\x00\x00\x00'
             b'\x02\x00\x01\x00\x00\x02\x02\x0C'
             b'\x0A\x00\x3B'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        cls.product = Products.objects.create(
            name='Продукт 1',
            slug='product1',
            category=cls.category,
            price=10,
            discount=0,
            quantity=1,
            image=uploaded,
        )
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
    
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
