from django.core.exceptions import ValidationError
from .usuarios.models import Usuario
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTER_REGEX = re.compile(r'^[a-zA-Z]+$')
RUT_REGEX = re.compile(r'^[0-9]+\-[kK0-9]+$')

def validarLongitud(cadena,campo,minlength = 3, maxlength = 10):
    if len(cadena) < minlength or len(cadena) > maxlength:
        raise ValidationError(f"{campo} debe tener entre {minlength} y {maxlength} caracteres")

def validarEmail(email):
    if not EMAIL_REGEX.match(email):     
        raise ValidationError("Email invalido")

def validarLetras(cadena,campo):
    if not LETTER_REGEX.match(cadena):
        raise ValidationError(f"{campo} debe contener solo letras y sin espacio")

def validarLongitudReturn(cadena,minlength = 3, maxlength = 10):
    if len(cadena) < minlength or len(cadena) > maxlength:
        return False
    return True

def validarEmailReturn(email):
    if not EMAIL_REGEX.match(email):     
       return False
    return True

def validarLetrasReturn(cadena):
    if not LETTER_REGEX.match(cadena):
        return False
    return True

def obtenerUsuario(id = None, email = None):
    try:
        if id:
            usuarioExiste = Usuario.objects.get(id = id)
        elif email:
            usuarioExiste = Usuario.objects.get(email__iexact = email)
    except:
        usuarioExiste = None
    return usuarioExiste
