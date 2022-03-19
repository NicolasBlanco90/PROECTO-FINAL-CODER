from django import forms

class UsuariosFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail= forms.EmailField()
    
class UsuariosBusqueda(forms.Form):
    nombre= forms.CharField(max_length=30)
    