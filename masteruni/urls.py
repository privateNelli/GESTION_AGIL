from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('dash', views.dash, name='dash'),
    path('signup', views.signup, name='signup'),
    path('inventario', views.inventario, name='inventario'),
    path('kit', views.kit, name='kit'),
    path('signout', views.signout, name='signout'),
]

