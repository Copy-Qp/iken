from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ClothesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clothes'
    verbose_name = _('Одежда')
