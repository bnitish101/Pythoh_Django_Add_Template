from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def room(request):
    return HttpResponse('Room')

def about(request):
    return HttpResponse('This is the about page.')