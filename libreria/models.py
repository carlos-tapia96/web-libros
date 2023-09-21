from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Libro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True, verbose_name=("Autor"))
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    created = models.DateField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    def __str__(self):
        return self.titulo






