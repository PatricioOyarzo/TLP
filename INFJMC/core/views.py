from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Home</h1>")
    return render(request, 'core/home.html')
    
def docente(request):
    return render(request, 'core/docente.html')
def carreras(request):
    carreras = Carrera.objects.all
    data ={
        'carreras': carreras
    }
    return render(request, 'core/carrera.html',data)   