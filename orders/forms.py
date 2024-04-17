import re

from django import forms
from django.core.exceptions import ValidationError


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.BooleanField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.BooleanField()

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not phone_number.isdigit():
            raise ValidationError('Номер телефона должен содержать только цифры')

        pattern = re.compile(r'^89\d{9}$')
        if not pattern.match(phone_number):
            raise ValidationError('Номер должен начинатсья с 89 и содержать 10 цифр')

        return phone_number

