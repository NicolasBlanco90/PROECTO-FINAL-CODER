from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    return render(request,'index/index.html',{})

def plantilla(request):
   return render(request,'index/plantilla.html')
