from http import HTTPStatus

from django.test import Client, TestCase


class MainURLTests(TestCase):
    """Тестирование путей приложения main."""

    @classmethod
    def setUpClass(cls):
        """Создание тестовых данных."""

        super().setUpClass()
        cls.guest_client = Client()

    def test_main_urls_exist_at_desired_location(self):
        """Проверка доступности адресов приложения main."""

        addresses = (
            '/',
            '/payment-delivery/',
            '/contacts/',
            '/work-group/',
        )
        for address in addresses:
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_main_urls_use_correct_template(self):
        """Проверка шаблонов приложения main."""

        templates = {
            '/': 'main/index.html',
            '/payment-delivery/': 'main/payment_delivery.html',
            '/contacts/': 'main/contacts.html',
            '/work-group/': 'main/work_group.html',
        }
        for address, expected_template in templates.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, expected_template)
