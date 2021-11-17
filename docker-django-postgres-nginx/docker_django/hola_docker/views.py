from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .models import ContactForm


def index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'Nosotros.html')


def home(request):
    return render(request, 'Home.html')


def sendform(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('phone') and\
                request.POST.get('date') and request.POST.get('message-1'):
            form = ContactForm()
            form.address = request.POST.get('email')
            form.name = request.POST.get('name')
            form.phone = request.POST.get('phone')
            form.date = request.POST.get('date')
            form.message = request.POST.get('message-1')
            form.save()
            return HttpResponseRedirect(reverse('Home'))
    else:
        return render(request, 'Contacto.html')
