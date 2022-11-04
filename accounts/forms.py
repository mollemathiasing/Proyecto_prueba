from dataclasses import fields
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User 
from django import forms       

#vamos a crear nuestro propio formulario usando como base el de django

class MiFormularioDeCreacion(UserChangeForm):
    
    email = forms.CharField(label= 'Email' , max_length=20)
    password1 = forms.CharField(label= 'Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        help_texts = {key: '' for key in fields}  