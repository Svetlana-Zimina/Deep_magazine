from django.test import TestCase

from goods.models import Categories, Products


class CategoriesModelTest(TestCase):
    """Тестирование модели Категория."""

    @classmethod
    def setUpClass(cls):
        """Задание тестовых данных."""

        super().setUpClass()
        cls.category = Categories.objects.create(
            name='категория 1',
            slug='category1'
        )

    def test_categories_verbose_name(self):
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

    def test_category_str(self):
        """Проверка метода __str__ модели Categories."""

        category = CategoriesModelTest.category
        expected_name = category.name
        self.assertEqual(expected_name, str(category))


class ProductsModelTest(TestCase):
    """Тестирование модели Продукты."""

    @classmethod
    def setUpClass(cls):
        """Задание тестовых данных."""

        super().setUpClass()
        cls.category = Categories.objects.create(
            name='категория 1',
            slug='category1'
        )
        cls.product = Products.objects.create(
            name='продукт',
            description='Описание продукта',
            price=300.99,
            discount=7,
            quantity=5,
            category=cls.category,
            slug='produkt'
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

    def test_product_str(self):
        """Проверка метода __str__ модели Products."""

        product = ProductsModelTest.product
        expected_name = product.name
        self.assertEqual(expected_name, str(product))

    def test_get_absolute_url(self):
        """Проверка метода get_absolute_url модели Products."""

        product = ProductsModelTest.product
        self.assertEquals(
            product.get_absolute_url(),
            f'/catalog/product/{product.slug}/'
        )

    def test_display_id(self):
        """Проверка метода display_id модели Products."""

        product = ProductsModelTest.product
        self.assertEquals(product.display_id(), '00001')

    def test_sell_price(self):
        """Проверка метода sell_price модели Products."""

        product = ProductsModelTest.product
        self.assertEquals(product.sell_price(), 279.92)
