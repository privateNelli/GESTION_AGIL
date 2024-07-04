from django import forms
from .models import *
from django.forms import ModelForm






class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class PasswordModelField(models.CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)

class UsuarioForm(ModelForm):
    n_usuario = forms.CharField(label="Usuario:", max_length=20)
    contrasena = forms.CharField(widget=PasswordModelField())
    class Meta:
        model = Usuario
        fields="__all__"

# class KitForm(ModelForm):
#     id_kit = forms.IntegerField()
#     nombre_kit = forms.CharField()
#     class Meta:
#         model = Kit
#         fields="__all__"



class InventarioForm(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    stock = forms.IntegerField()
    fecha_venc =  forms.DateField()
    id_kit = forms.IntegerField()