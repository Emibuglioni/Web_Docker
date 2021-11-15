from django.urls import path

from hola_docker import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('index/Home.html', views.home, name='Home'),
    path('index/Nosotros.html', views.nosotros, name='Nosotros'),
    path('index/Contacto.html', views.contacto, name='Contacto'),
    path('index/RegistrarForm', views.ContactFormView.contact, name='RegistrarForm'),
    path('index/ProcesarForm', views.ContactFormView.process_form, name='ProcesarForm'),
]
