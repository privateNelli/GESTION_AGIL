from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('dash', views.dash, name='dash'),
    
]

