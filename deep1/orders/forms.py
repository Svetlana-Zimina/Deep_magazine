import re

from django import forms

DELIVERY_TYPES = (
    ('-', '-'),
    ('Яндекс доставка', 'Яндекс доставка'),
    ('Почта', 'Почта'),
)

PICKUP_PLACES = (
    ('-', '-'),
    ('«Посольство Уральских гор»', '«Посольство Уральских гор»'),
    ('«Территория странствий»', '«Территория странствий»'),
    ('«Центр путешественников»', '«Центр путешественников»'),
    ('Клуб СГС', 'Клуб СГС'),
    ('Магазин SportX', 'Магазин SportX'),
    ('Пермский спелеоклуб', 'Пермский спелеоклуб'),
    ('«Земля приключений»', '«Земля приключений»'),
    ('«Вертикаль»', '«Вертикаль»'),
    ('«Геккон»', '«Геккон»')
)


class CreateOrderForm(forms.Form):
    """Форма оформления заказа."""

    user_first_name = forms.CharField(max_length=255)
    user_last_name = forms.CharField(max_length=255)
    phone = forms.CharField()
    email = forms.CharField(max_length=255)
    requires_delivery = forms.BooleanField(required=False)
    delivery_type = forms.ChoiceField(
        choices=DELIVERY_TYPES,
        required=False
    )
    pickup_place = forms.ChoiceField(
        choices=PICKUP_PLACES,
        required=False
    )
    delivery_address = forms.CharField(max_length=255, required=False)
    send_to_email = forms.BooleanField(required=False)

    def clean_phone(self):
        """Проверка номера телефона на соответствие шаблону."""

        data = self.cleaned_data['phone']

        pattern = re.compile(r"^((\+7|7|8)+([0-9]){10})$")
        if not pattern.match(data):
            raise forms.ValidationError(
                "Неверный формат номера. Правильный формат: +7ХХХХХХХХХХ"
            )

        return data
