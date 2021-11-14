from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'Nosotros.html')

def contacto(request):
    return render(request, 'Contacto.html')

def home(request):
    return render(request, 'Home.html')