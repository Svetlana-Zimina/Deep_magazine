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

    user_first_name = forms.CharField(max_length=255)
    user_last_name = forms.CharField(max_length=255)
    phone = forms.CharField()
    email = forms.CharField(max_length=255)
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_type = forms.ChoiceField(
        choices=DELIVERY_TYPES,
        required=False
    )
    pickup_place = forms.ChoiceField(
        choices=PICKUP_PLACES,
        required=False
    )
    delivery_address = forms.CharField(max_length=255, required=False)
    
    def clean_phone(self):
        data = self.cleaned_data['phone']

        pattern = re.compile(r"^((\+7|7|8)+([0-9]){10})$")
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
