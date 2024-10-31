from django.shortcuts import render
from .servicios import solicitar
from .servicios import obtenersms
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.
def principal(request):
    return render(request, 'ejercicios/principal.html', {'datos': solicitar})

def mensajes(request):
    return render(request, 'ejercicios/mensajes.html', {'mensajeria': obtenersms})


def archivos(request):
    if request.method == 'POST':
        form=FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo=request.FILES['archivo']
            insert=Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"ejercicios/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"ejercicios/archivos.html",{'archivo':Archivos})