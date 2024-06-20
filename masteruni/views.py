from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def dash(request):
    if request.method == "GET":
        inventario=Inventario.objects.raw('SELECT * FROM inventarios_inventario')
        context={"inventario":inventario}
        return render(request, 'masteruni/dash.html', context)




def signin(request):
    if request.method == 'GET':
        return render(request, 'masteruni/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'masteruni/login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')
        


def index(request):
    return render(request, 'masteruni/index.html')
