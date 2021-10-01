from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from apps.validaciones import obtenerUsuario, validarLongitud, validarEmail, validarLetras

class FormularioRegistroSU(forms.ModelForm):
    confirmarPassword = forms.CharField(max_length=255, label="Confirmar Password")
    confirmarPassword.widget = forms.PasswordInput()

    class Meta:
        model = Usuario
        fields = ["first_name", "last_name","is_superuser", "email","password","confirmarPassword","company"]

        widgets = {
            "password" : forms.PasswordInput(),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        validarLetras(first_name,"first_name")
        validarLongitud(first_name,"nombre",2,15)
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        validarLetras(last_name,"last_name")
        validarLongitud(last_name,"apellido",2,15)
        return last_name
    
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        validarEmail(email)
        usuario = obtenerUsuario(email=email)
        if usuario:
            raise ValidationError("Correo ya existe")
        return email

    def clean(self):
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirmarPassword"]
        if len(password) < 8 or len(password) > 50:
            raise ValidationError({"password" : f"password debe tener entre 8 y 50 caracteres."})
        if password != confirm:
            raise ValidationError({"password" : "Las contraseñas no coinciden."})

class FormularioRegistro(FormularioRegistroSU):

    class Meta:
        model = Usuario
        fields = ["first_name", "last_name","email","password","confirmarPassword","company"]
    
        widgets = {
            "password" : forms.PasswordInput(),
        }

class FormularioEditar(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "company"]
