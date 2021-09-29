from django import forms
from .models import Company
from apps.validaciones import validarLongitud

class FormularioCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["nombre"]

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        validarLongitud(nombre,"nombre",2,15)
        return nombre