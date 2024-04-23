import re
from django import forms


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
    delivery_address = forms.CharField(max_length=255, required=False)
    
    def clean_phone(self):
        data = self.cleaned_data['phone']

        pattern = re.compile(r"[\d]{3}-[\d]{3}-[\d]{2}-[\d]{2}")
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
