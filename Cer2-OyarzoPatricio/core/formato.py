from django import forms
from .models import Comunicado

class ComunicadoForm(forms.ModelForm):
    modelo = Comunicado
    validacion = ['titulo','contenido','nivel','categoria']

