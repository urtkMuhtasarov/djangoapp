from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('home')

def index(request):
    return render(request, 'home.html')