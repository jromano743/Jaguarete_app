#Archivo que va a redireccionar a la aplicacion
#Responde a las funciones de views.py de la aplicacion 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('acerca-de', views.acercaDe, name="acerca-de"),
    path('carrito', views.carrito, name="carrito"),
    path('login', views.login, name="login"),
    path('producto', views.producto, name="producto"),
    path('nuevo-producto', views.nuevoProducto, name="nuevo-producto"),
    path('registro', views.registro, name="registro"),
    path('resultado-busqueda', views.resultadoBusqueda, name="resultado-busqueda")
]