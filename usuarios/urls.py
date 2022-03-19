
from sys import path_importer_cache
from django.urls import path
from . import views

urlpatterns = [
    path('usuario/crear/',views.crear_usuario,name='crear_usuario'),
    path('usuarios',views.lista_usuario,name='lista_usuario'),
    ]
