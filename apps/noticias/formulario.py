from django import forms
from apps.keywords.models import Keyword

class FormularioData(forms.ModelForm):
    cantidad = forms.IntegerField()

    class Meta:
        model = Keyword
        fields = ["grupo","cantidad"]