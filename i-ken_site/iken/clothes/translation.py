from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Clothes)
class ClothesTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'price')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)