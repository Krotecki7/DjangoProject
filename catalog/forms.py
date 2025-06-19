from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from .models import Product
from .constants import forbidden_words


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "image",
            "category",
            "price",
        )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название игры"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание игры"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену"}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name").lower()
        for word in forbidden_words:
            if word in name:
                raise ValidationError("Запрещенное слово в названии")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description").lower()
        for word in forbidden_words:
            if word in description:
                raise ValidationError("Запрещенное слово в описании")
        return description


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ["is_active"]
