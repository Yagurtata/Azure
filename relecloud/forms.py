from django import forms
from .models import Crucero

class CruceroForm(forms.ModelForm):
    class Meta:
        model = Crucero
        fields = ['tipo_crucero', 'duracion_dias', 'precio', 'fecha_salida']
