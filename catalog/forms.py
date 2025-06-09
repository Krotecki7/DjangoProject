from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from .models import Product
from .constants import forbidden_words


def valid_name(name):
    if name.lower in forbidden_words:
        raise ValidationError('Запрещенное слово в названии', params={'name': name})


def valid_description(description):
    for word in forbidden_words:
        if word in description.lower:
            raise ValidationError('Вы используете запрещенное слово в описание', params={'description': description})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        name = forms.CharField(max_length=100, validators=[valid_name])
        description = forms.CharField(max_length=1000, validators=[valid_description])
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название игры'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание игры'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower in forbidden_words:
            raise ValidationError('Запрещенное слово в названии')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description:
                raise ValidationError('Запрещенное слово в описании')
        return description

