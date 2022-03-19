from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request,'index/index.html',{})

def plantilla(request):
   return render(request,'index/plantilla.html')