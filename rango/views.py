from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    contextDict = {
        'aboldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/index.html', context=contextDict)

def about(request):
    return render(request, 'rango/about.html')
