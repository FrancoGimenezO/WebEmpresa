from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length = 100, verbose_name = "Nombre")
    created = models.TimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.TimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.TextField(max_length = 100, verbose_name = "Nombre")
    content = models.TextField(verbose_name= "Contenido")
    published = models.DateTimeField(verbose_name="Hora de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author =models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.TimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.TimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title