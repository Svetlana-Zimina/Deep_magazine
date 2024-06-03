from django.test import TestCase, Client
from django.urls import reverse


class MainViewsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        """Создание тестовых данных."""

        super().setUpClass()
        cls.guest_client = Client()
    
    def test_main_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        
        templates_pages_names = {
            'main/index.html': reverse('main:index'),
            'main/payment_delivery.html': reverse('main:payment-delivery'),
            'main/contacts.html': reverse('main:contacts'),
            'main/work_group.html': reverse('main:work-group'),
        }
        
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
    
    def test_task_list_page_show_correct_context(self):
        """Шаблоны приложения main сформированы с правильным контекстом."""

        reverse_names = {
            reverse('main:index'): 'Бездна - Главная',
            reverse('main:payment-delivery'): 'Бездна - Оплата и доставка',
            reverse('main:contacts'): 'Бездна - Контакты',
            reverse('main:work-group'): 'Бездна - Над журналом работают',
        }
        
        for reverse_name, title in reverse_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertEqual(response.context['title'], title)
