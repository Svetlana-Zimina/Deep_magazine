from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from carts.utils import get_user_carts

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    cart_items = get_user_carts(request)

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
                            '\nСпасибо за заказ!\n'
                            '\nВозникшие вопросы пишите в группу ВК '
                            '(в личные сообщения): vk.com/speleonews '
                            'с указанием имени, фамилии и номера заказа'
                        )
                        send_mail(
                            f'Журнал "Бездна"_Заказ №{order.id}',
                            mail_text,
                            'Zima271985@yandex.ru',
                            [order.email],
                            fail_silently=False,
                        )

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        
                        return redirect('main:index')
                    
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('main:index')
    else:
        form = CreateOrderForm()

    context = {
        'title': 'Бездна - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)
