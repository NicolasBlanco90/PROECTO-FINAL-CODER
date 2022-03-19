from django.shortcuts import redirect, render

from .forms import UsuariosFormulario, UsuariosBusqueda, BlogFormulario, MensajeFormulario
from .models import usuario, blog, mensaje

# Create your views here.
def crear_usuario(request):
    
    if request.method == 'POST':
        form = UsuariosFormulario(request.POST)
        
        if form.is_valid():
           data = form.cleaned_data
           Usuario = usuario(nombre=data['nombre'],apellido=data['apellido'],mail=data['mail'])
           Usuario.save()
           return redirect('plantilla')
    
    form = UsuariosFormulario()
    return render(request,'usuarios/crear_usuario.html',{'form': form})


def lista_usuario(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        usuarios = usuario.objects.filter(nombre__icontains= nombre_a_buscar)
    else:
        usuarios = usuario.objects.all()
    
    form = UsuariosBusqueda()
    return render(request,'usuarios/lista_usuario.html',{'form': form, 'usuarios' : usuarios})



def crear_blog(request):
    
    if request.method == 'POST':
        form = BlogFormulario(request.POST)
        
        if form.is_valid():
           data = form.cleaned_data
           Blog = blog(blog=data['blog'])
           Blog.save()
           return redirect('plantilla')
    
    form = BlogFormulario()
    return render(request,'usuarios/crear_blog.html',{'form': form})


def crear_mensaje(request):
    
    if request.method == 'POST':
        form = MensajeFormulario(request.POST)
        
        if form.is_valid():
           data = form.cleaned_data
           Mensaje = mensaje(mensaje=data['mensaje'])
           Mensaje.save()
           return redirect('plantilla')
    
    form = MensajeFormulario()
    return render(request,'usuarios/crear_mensaje.html',{'form': form})