from django import forms
from .models import Keyword

class FormularioKeyword(forms.ModelForm):

    class Meta:
        model = Keyword
        fields = ["grupo","keywords"]