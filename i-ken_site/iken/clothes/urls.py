from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', categories, name='category'),
    path('clothes/<int:clothes_id>/', clothes, name='clothes'),
]