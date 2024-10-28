from django.contrib import admin
from django.urls import path
from ejercicios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name='Principal'),
    path('mensajes/', views.mensajes, name='mensajes'),

]