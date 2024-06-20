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


class InventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields="__all__"