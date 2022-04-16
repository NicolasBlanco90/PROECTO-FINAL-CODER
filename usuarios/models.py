from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    material = RichTextField(blank= True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class blog(models.Model):
    titulo = models.CharField(max_length=30,blank= True, null=True)
    subtitulo = models.CharField(max_length=30,blank= True, null=True)
    imagen_blog= models.ImageField(upload_to='imagen_blog',blank=True, null=True)
    blog = RichTextField(blank= True, null=True)
    fecha_creacion_blog = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.blog}'

    
class mensaje(models.Model):
    mensaje = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.mensaje}'