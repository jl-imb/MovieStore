from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
path('', views.index, name='home.index'),
]

def index(request):
    return render(request, 'home/index.html')