from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import BooleanField

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'phone_number', 'country', 'image', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите почту"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите номер телефона"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["country"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Придумайте пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите пароль"}
        )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Ваша почта'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
            self.fields[field].widget.attrs.update({'class': 'form-control'})
