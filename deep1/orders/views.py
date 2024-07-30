from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.utils import get_user_carts

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from dotenv import load_dotenv
import os

load_dotenv()


class CreateOrderView(FormView):

    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                cart_items = get_user_carts(self.request)

                if cart_items.exists():
                    # Создать заказ
                    order = Order.objects.create(
                        **form.cleaned_data
                    )
                        
                    mail_text = (
                        f'{order.user_first_name}, '
                        'Вы сделали заказ на сайте журнала "Бездна":\n\n'
                    )

                    # Создать заказанные товары
                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                    В наличии - {product.quantity}')

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.quantity -= quantity
                        product.save()

                        mail_text = mail_text + f'{product.name} - {quantity} шт' + '\n'

                    # Отправка подтверждения на электронную почту
                    mail_text += (
                        f'\nВариант доставки: {order.delivery_type}\n'
                        f'Адрес доставки: {order.delivery_address}\n'
                        f'Пункт самовывоза: {order.pickup_place}\n'
                        '\nСпасибо за заказ!\n'
                        '\nВозникшие вопросы пишите в группу ВК '
                        '(в личные сообщения): vk.com/speleonews '
                        'с указанием имени, фамилии и номера заказа'
                    )
                    send_mail(
                        f'Журнал "Бездна"_Заказ №{order.id}',
                        mail_text,
                        os.getenv('EMAIL_HOST_USER'),
                        [order.email],
                        fail_silently=False,
                    )

                    send_mail(
                        f'Новый_Заказ №{order.id}',
                        f'Появился новый заказ: №{order.id}',
                        os.getenv('EMAIL_HOST_USER'),
                        ['Zima271985@yandex.ru'],
                        fail_silently=False,
                    )

                    # Очистить корзину пользователя после создания заказа
                    cart_items.delete()

                    messages.success(self.request, 'Заказ оформлен!')
                        
                    return redirect('main:index')
                    
        except ValidationError as e:
            messages.success(self.request, str(e))
            return redirect('main:index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Возникли трудности при оформлении заказа!')
        return redirect('orders:create-order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бездна - Оформление заказа'
        context['order'] = True
        return context


# def create_order(request):
#     if request.method == 'POST':
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     cart_items = get_user_carts(request)

#                     if cart_items.exists():
#                         # Создать заказ
#                         order = Order.objects.create(
#                             **form.cleaned_data
#                         )
                        
#                         mail_text = (
#                             f'{order.user_first_name}, '
#                             'Вы сделали заказ на сайте журнала "Бездна":\n\n'
#                         )

#                         # Создать заказанные товары
#                         for cart_item in cart_items:
#                             product = cart_item.product
#                             name = cart_item.product.name
#                             price = cart_item.product.sell_price()
#                             quantity = cart_item.quantity

#                             if product.quantity < quantity:
#                                 raise ValidationError(f'Недостаточное количество товара {name} на складе\
#                                                        В наличии - {product.quantity}')

#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                             product.quantity -= quantity
#                             product.save()

#                             mail_text = mail_text + f'{product.name} - {quantity} шт' + '\n'

#                         # Отправка подтверждения на электронную почту
#                         mail_text += (
#                             f'\nВариант доставки: {order.delivery_type}\n'
#                             f'Адрес доставки: {order.delivery_address}\n'
#                             f'Пункт самовывоза: {order.pickup_place}\n'
#                             '\nСпасибо за заказ!\n'
#                             '\nВозникшие вопросы пишите в группу ВК '
#                             '(в личные сообщения): vk.com/speleonews '
#                             'с указанием имени, фамилии и номера заказа'
#                         )
#                         send_mail(
#                             f'Журнал "Бездна"_Заказ №{order.id}',
#                             mail_text,
#                             os.getenv('EMAIL_HOST_USER'),
#                             [order.email],
#                             fail_silently=False,
#                         )

#                         # Очистить корзину пользователя после создания заказа
#                         cart_items.delete()

#                         messages.success(request, 'Заказ оформлен!')
                        
#                         return redirect('main:index')
                    
#             except ValidationError as e:
#                 messages.success(request, str(e))
#                 return redirect('main:index')
#     else:
#         form = CreateOrderForm()

#     context = {
#         'title': 'Бездна - Оформление заказа',
#         'form': form,
#         'orders': True,
#     }
#     return render(request, 'orders/create_order.html', context=context)
