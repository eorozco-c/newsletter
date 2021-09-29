from django import forms
from .models import TipoMedio, Medio

class FormularioTipoMedio(forms.ModelForm):

    class Meta:
        model = TipoMedio
        fields = ["nombre"]

class FormularioMedio(forms.ModelForm):

    class Meta:
        model = Medio
        fields = ["nombre", "tipo"]