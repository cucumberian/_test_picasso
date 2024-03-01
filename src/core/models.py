from django.db import models


class File(models.Model):
    file = models.FileField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    processed = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
