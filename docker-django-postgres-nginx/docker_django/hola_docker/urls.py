from django.urls import path

from hola_docker import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('index/Home.html',views.home, name='Home'),
    path('index/Nosotros.html',views.nosotros, name='Nosotros'),
    path('index/Contacto.html',views.contacto, name='Contacto'),
]