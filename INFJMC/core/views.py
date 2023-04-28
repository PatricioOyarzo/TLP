from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("<h1>Home</h1>")
    return render(request, 'core/home.html')
    
def docente(request):
    return render(request, 'core/docente.html')
def carrera(request):
    return render(request, 'core/carrera.html')