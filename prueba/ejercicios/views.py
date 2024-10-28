from django.shortcuts import render
from .servicios import solicitar
from .servicios import obtenersms

# Create your views here.
def principal(request):
    return render(request, 'ejercicios/principal.html', {'datos': solicitar})

def mensajes(request):
    return render(request, 'ejercicios/mensajes.html', {'mensajeria': obtenersms})
