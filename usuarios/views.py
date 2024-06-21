from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistroForm
from django.contrib import messages  # Importar el módulo de mensajes

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                return redirect('panel')
            else:
                return render(request, 'usuarios/login.html', {'form': form, 'error': 'Credenciales inválidas.'})
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def panel(request):
    return render(request, 'usuarios/panel.html', {'user': request.user})
