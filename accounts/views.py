from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm          #traemos el formulario q nos brinda django
from django.contrib.auth import login
from accounts.forms import MiFormularioDeCreacion

def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():     #si es un usuario de nuestra base de datos pasa y hace el redirect, sino pasa al else 
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('index')     #una vez logueado me redirige a index
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario}) 


def registrar(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()           #crea el usuario nuevo al guardarlo
            return redirect ('index')
    else:
        formulario = MiFormularioDeCreacion()
    return render(request, 'accounts/registrar.html', {'formulario': formulario}) 