from django import forms
from .models import TipoMedio

class FormularioTipoMedio(forms.ModelForm):

    class Meta:
        model = TipoMedio
        fields = ["nombre"]