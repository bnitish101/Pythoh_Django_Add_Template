from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('homeFormProject/', views.homeFormProject, name = 'homeFormProject'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('about/', views.about, name='about'),
]