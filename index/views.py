from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse ('<h1>BIENVENIDO A BLOGLANDIA</h1>')

def plantilla(request):
    
   template = loader.get_template('plantilla.html')
   
   datos = {
       'lista': ['primer', 'segundo'],
       'nombre': 'juan'
   }
   
   plantillauno = template.render(datos)
   
   return HttpResponse (plantillauno)
    