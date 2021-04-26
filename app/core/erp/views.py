from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'danilo'
    }
    return render(request, 'index.html', data)