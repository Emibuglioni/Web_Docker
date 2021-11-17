from django.urls import path

from hola_docker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home.html', views.home, name='Home'),
    path('Nosotros.html', views.nosotros, name='Nosotros'),
    path('Contacto.html', views.sendform, name='Contacto'),
]
