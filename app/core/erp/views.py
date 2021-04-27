
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def myfirstview(request):
    data = {
        'name': 'danilo',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)

def secondview(request):
    data = {
        'name': 'danilo',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
