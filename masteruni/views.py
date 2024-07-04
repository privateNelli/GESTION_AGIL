from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import *
from .models import *

# Create your views here.

def dash(request):
    if request.method == "GET":
        inventario=Inventario.objects.raw('SELECT * FROM masteruni_inventario')
        context={"inventario":inventario}
        return render(request, 'masteruni/dash.html', context)

# def dash2(request):
#     if request.method == "GET":
#         kit=Kit.objects.raw('SELECT * FROM masteruni_kit')
#         context={"kit":kit}
#         return render(request, 'masteruni/dash2.html', context)



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
        
def inventario(request):
    if request.method == "POST":
        form = InventarioForm
        context = {'form':form, 'msj':'Error, intente de nuevo...'}
        Inventario.objects.create(id=request.POST["id"], 
                               nombre=request.POST["nombre"], 
                               categoria=request.POST["categoria"], 
                               stock=request.POST["stock"], 
                               fecha_venc=request.POST["fecha_venc"])
        return render(request, 'masteruni/inventario.html', context)
    else:
        return render(request, 'masteruni/inventario.html', {'form':InventarioForm})
    
# def kit(request):
#     if request.method == "POST":
#         form = KitForm
#         context = {'form':form, 'msj':'Error, Intente de nuevo...'}
#         Kit.objects.create(id_kit=request.POST["id_kit"],
#                            nombre_kit=request.POST["nombre_kit"])
#         return render(request, 'masteruni/kit.html', context)
#     else:
#         return render(request, 'masteruni/kit.html', {'form':KitForm})        
        


def index(request):
    return render(request, 'masteruni/index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'masteruni/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'masteruni/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'masteruni/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })


def signout(request):
    logout(request)
    return redirect('index')

