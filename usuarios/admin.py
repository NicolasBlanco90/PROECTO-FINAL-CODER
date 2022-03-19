from django.contrib import admin
from usuarios.models import blog, mensaje, usuario

# Register your models here.
admin.site.register(usuario)
admin.site.register(blog)
admin.site.register(mensaje)