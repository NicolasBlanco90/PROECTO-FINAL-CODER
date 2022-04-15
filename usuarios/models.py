from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    material = models.CharField(max_length=500, null=True, default='')
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class blog(models.Model):
    blog = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.blog}'

    
class mensaje(models.Model):
    mensaje = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.mensaje}'