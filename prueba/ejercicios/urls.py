from django.contrib import admin
from django.urls import path
from ejercicios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name='Principal'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('subir/', views.archivos, name="Subir"),
]

# ESTE URL NO ES LA RAIZ DEL PROYECTO, AQUI NO HACER EL RUTEO