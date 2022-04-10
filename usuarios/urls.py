
from sys import path_importer_cache
from django.urls import path
from . import views

urlpatterns = [
    path('usuarios',views.lista_usuario,name='usuarios'),
    path('usuario/crear/',views.crear_usuario,name='crear_usuario'),
    path('usuario/detalle/<int:pk>',views.DetalleUsuario.as_view(),name='detalle_usuario'),
    path('usuario/editar/<int:pk>',views.EditarUsuario.as_view(),name='editar_usuario'),
    path('usuario/borrar/<int:pk>',views.BorrarUsuario.as_view(),name='borrar_usuario'),
    path('blog/crear/',views.crear_blog,name='crear_blog'),
    path('mensaje/crear/',views.crear_mensaje,name='crear_mensaje'),
    ]
