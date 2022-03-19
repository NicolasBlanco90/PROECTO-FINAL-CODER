from django import forms

from usuarios.models import mensaje

class UsuariosFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail= forms.EmailField()

    
class UsuariosBusqueda(forms.Form):
    nombre= forms.CharField(max_length=30)

   
class BlogFormulario(forms.Form):
    blog= forms.CharField(max_length=500)

    
class MensajeFormulario(forms.Form):
    mensaje= forms.CharField(max_length=500)
    