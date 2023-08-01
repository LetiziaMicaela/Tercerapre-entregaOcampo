from django import forms
from .models import Gatito, Adoptante, Personal


class GatitoForm(forms.ModelForm):
    class Meta:
        model = Gatito
        fields = ['nombre', 'raza', 'edad']

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['nombre', 'edad', 'direccion','correo']

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre', 'puesto', 'horario']

#formulario de busqueda 
from django import forms

class BuscarGatitoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Gatito", max_length=100)

