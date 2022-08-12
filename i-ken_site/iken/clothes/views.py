from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *

def main(request):
    catigories = Category.objects.all()

    con = {
        'title': 'I-Ken',
        'catigories': catigories,
    }

    return render(request, 'clothes/main.html', context=con)

def categories(request, cat_id):
    clothes = Clothes.objects.filter(cat_id = cat_id, is_published = True)
    catigories = Category.objects.all()

    con = {
        'title': 'I-Ken',
        'clothes': clothes,
        'catigories': catigories,
        'cat_id': cat_id,
    }

    return render(request, 'clothes/categories.html', context=con)

def clothes(request, clothes_id):
    clothes = get_object_or_404(Clothes, pk=clothes_id, is_published = True)

    con = {
        'title': 'I-Ken',
        'clothes': clothes,
    }

    return render(request, 'clothes/clothes.html', context=con)

def about(request):

    con = {
        'title': 'О нас'
    }

    return render(request, 'clothes/about.html', context=con)

def PageNotFound(request, exception):
    return render(request, 'clothes/PageNotFounded.html')
