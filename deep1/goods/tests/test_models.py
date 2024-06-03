from django.test import TestCase
from goods.models import Categories, Products


class CategoriesModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Categories.objects.create(
            name='Имя тестовой категории',
            slug='test-category'
        )
    
    def test_verbose_name(self):
        """verbose_name в полях Categories совпадает с ожидаемым."""
        category = CategoriesModelTest.category
        field_verboses = {
            'name': 'Название',
            'slug': 'URL',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    category._meta.get_field(field).verbose_name,
                    expected_value
                )


class ProductsModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Products.objects.create(
            name='Продукт',
            description='Описание продукта',
            price=100,
            discount=0,
            quantity=5,
        )
    
    def test_verbose_name(self):
        """verbose_name в полях Products совпадает с ожидаемым."""
        product = ProductsModelTest.product
        field_verboses = {
            'name': 'Название',
            'slug': 'URL',
            'description': 'Описание',
            'image': 'Изображение',
            'image_2': 'Изображение 2',
            'image_3': 'Изображение 3',
            'price': 'Цена',
            'discount': 'Скидка в процентах',
            'quantity': 'Количество',
            'category': 'Категория',
            'pdf_file': 'Файл PDF'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    product._meta.get_field(field).verbose_name,
                    expected_value
                )
    
    def test_get_absolute_url(self):
        product = ProductsModelTest.product
        self.assertEquals(product.get_absolute_url(), '/catalog/product/product')
