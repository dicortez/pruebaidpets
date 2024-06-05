from sqlite3 import IntegrityError
from django.contrib.auth import  authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from .forms import LoginForm
from django.contrib.auth import login as auth_login 

# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')
def nosotros(request):
    return render (request,'paginas/nosotros.html')

def Mascotas(request):
    return render(request, 'Mascotas/index.html')

def registrar_mascotas(request):
    return render(request, 'Mascotas/registrar_mascotas.html')

def editar_mascotas(request):
    return render(request, 'Mascotas/editar_mascotas.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('inicio')  # Redirige a la página de inicio después de iniciar sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'paginas/signup.html', {"form": form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Iniciar sesión si las credenciales son válidas
                return redirect('inicio')
            else:
                # Mensaje de error si las credenciales son inválidas
                return render(request, 'paginas/login.html', {'form': form, 'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        form = LoginForm()
    return render(request, 'paginas/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)  # Cerrar sesión del usuario
    return redirect('inicio')

