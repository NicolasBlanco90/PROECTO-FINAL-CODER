from django.contrib import admin

from usuarios.models import estudiantes, freelancers, profesionales, usuario

# Register your models here.
admin.site.register(usuario)
admin.site.register(profesionales)
admin.site.register(estudiantes)
admin.site.register(freelancers)