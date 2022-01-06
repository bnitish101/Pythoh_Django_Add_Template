from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Room Name One'},
    {'id':2, 'name':'Room Name Two'},
    {'id':3, 'name':'Room Name Three'},
]

def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')

def about(request):
    return render(request, 'about.html')