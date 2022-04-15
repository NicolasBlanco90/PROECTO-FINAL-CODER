from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login, registrarse, edit_user
 
urlpatterns = [
    path('login/', login, name='login'),
    path('editar/', edit_user, name='edit_user'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
 ]