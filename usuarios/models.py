from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class profesionales(usuario):
    profesion = models.CharField(max_length=50)
    
class estudiantes(usuario):
    escuela = models.CharField(max_length=50)
    
class freelancers(usuario):
    especialidad = models.CharField(max_length=50)