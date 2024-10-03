from django import forms
from .models import ValidacionResultado

class ArchivoCSVForm(forms.ModelForm):
    class Meta:
        model = ValidacionResultado
        fields = ['archivo']