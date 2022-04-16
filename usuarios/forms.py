from django import forms
from ckeditor.fields import RichTextFormField

from usuarios.models import mensaje

class UsuariosFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail= forms.EmailField()
    material = RichTextFormField(required=False)

    
class UsuariosBusqueda(forms.Form):
    nombre= forms.CharField(max_length=30)

   
class BlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    subtitulo = forms.CharField(max_length=30, required=False)
    imagen_blog = forms.ImageField(required=False)
    blog= RichTextFormField(required=False)

    
class MensajeFormulario(forms.Form):
    mensaje= forms.CharField(max_length=500)
    
class BlogBusqueda(forms.Form):
    nombre= forms.CharField(max_length=30)