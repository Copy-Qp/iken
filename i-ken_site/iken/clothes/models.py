from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Clothes(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    content = models.TextField(verbose_name=_('Текст'))
    photo = models.ImageField(upload_to="photos/%Y/%m/d/", verbose_name=_('Фото'))
    price = models.CharField(max_length=255, verbose_name=_('Цена'))
    time_create = models.DateField(auto_now_add=True, verbose_name=_('Время создания'))
    time_update = models.DateField(auto_now=True, verbose_name=_('Время обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликован'))
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name=_('Категория'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("clothes", kwargs={"clothes_id": self.pk})

    class Meta:
        verbose_name = _('Одежда')
        verbose_name_plural = _('Одежда')
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name=_('Имя'))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['id',]
