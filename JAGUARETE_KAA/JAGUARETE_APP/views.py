from django.shortcuts import render
from django.http import HttpResponse #Para peticiones HTTP

# Create your views here.
def acercaDe(req):
    return render(req, "acerca-de/acerca-de.html")

def carrito(req):
    return render(req, "carrito/carrito.html")

def index(req):
    return render(req, "index/index.html")

def login(req):
    return render(req, "login/login.html")

def producto(req):
    return render(req, "producto/producto.html")

def nuevoProducto(req):
    return render(req, "nuevo-producto/nuevo-producto.html")

def registro(req):
    return render(req, "registro/registro.html")

def resultadoBusqueda(req):
    return render(req, "resultado-busqueda/resultado-busqueda.html")

#Pasar el contexto a travez de un diccionario como tercer parametro
#Se accede a las sesiones por medio de request.session["item"], los elementos de la sesion son un string

#PAra trabajar con sesiones se debe usar manae.py migrate para crear la tabla de sesiones