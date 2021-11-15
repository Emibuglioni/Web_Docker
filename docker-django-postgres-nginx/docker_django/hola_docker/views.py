from django.shortcuts import render
from django.http import HttpRequest

from .models import ContactForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'Nosotros.html')

def contacto(request):
    return render(request, 'Contacto.html')

def home(request):
    return render(request, 'Home.html')

def ContactForm(request):
    if request.method == "POST":
        address = request.POST["txtAddress"]
        name = request.POST["txtName"]
        phone = request.POST["txtPhone"]
        date = request.POST["txtDate"]
        message = request.POST["txtMessage"]
        return render(request, 'index.html')
    return render(request, 'Contacto.html')


class ContactFormView(HttpRequest):

    def contact(request):
        form = ContactForm()
        return render(request, '', {'form': form})

    def process_form(request):
        form = ContactForm()
        if form.is_valid():
            form.save()
            form = ContactForm()

        return render(request, 'index.html', {'form': form, 'message': 'OK'})
