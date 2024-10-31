from django.db import models

# Create your models here.
class Archivos(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField(null=True, blank=True)
    archivo=models.FileField(upload_to="archivos",
                             null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Archivo"
        verbose_name_plural="Archivos"
        ordering=["-created"]

    def __str__(self):
        return self.titulo