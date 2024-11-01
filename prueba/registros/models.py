from django.db import models

# Create your models here.

class Alumnos (models.Model):#Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="codigo")#texto corto
    nombre = models.CharField(max_length=50)#texto largo
    carrera = models.CharField(max_length=50)
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)#fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre
    #indica que se mostrara el nombre como valor en la tabla    