from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    image = models.ImageField(upload_to="blogs_images/", blank=True, null=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_valid = models.BooleanField(verbose_name="Признак публикации")
    views_count = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.name
