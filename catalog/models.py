from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="screenshots/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория товара",
        blank=True,
        null=True,
        related_name='products'
    )
    price = models.IntegerField(verbose_name="Цена")
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ad = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего обновления"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_ad", "updated_ad"]

    def __str__(self):
        return self.name
