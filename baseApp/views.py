from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Room Name One'},
    {'id':2, 'name':'Room Name Two'},
    {'id':3, 'name':'Room Name Three'},
]

def home(request):
    context = {'rooms' : rooms}
    return render(request, 'baseApp/home.html', context) # this will render form base directory inside baseApp directory application
    # return render(request, 'home.html', context)  # this will render form base directory project

def homeFormProject(request):
    context = {'rooms' : rooms}
    # return render(request, 'baseApp/home.html', context) # this will render form base directory inside baseApp directory application
    return render(request, 'home.html', context)  # this will render form base directory project

def room(request, pk):
    context = None
    for room in rooms:
        if room['id'] == int(pk):   # to get value form dic. we can use [] or get method
            context = {'room': room.get('name')} # to get value form dic. we can use [] or get method
        
    return render(request, 'baseApp/room.html', context)

def about(request):
    return render(request, 'baseApp/about.html')