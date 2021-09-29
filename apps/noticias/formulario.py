from django import forms

class FormularioData(forms.Form):
    keyword = forms.CharField(max_length=255)
    cantidad = forms.IntegerField()