from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Почта")
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name="Имя пользователя", unique=True)
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="Номер телефона",
    )
    country = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Страна"
    )
    image = models.ImageField(
        upload_to="users_image/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
