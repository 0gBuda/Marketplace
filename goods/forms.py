# goods/forms.py
from django import forms
from .models import Products, Categories


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'name',
            'descriptions',
            'price',
            'discount',
            'category',
            'quantity',
            'image',
        ]

    name = forms.CharField()
    descriptions = forms.CharField()
    price = forms.DecimalField()
    discount = forms.DecimalField()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    image = forms.ImageField()