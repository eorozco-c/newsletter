from django.db import models
from apps.companies.models import Company

# Create your models here.
class TipoMedio(models.Model):
    nombre = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.nombre
        
class Medio(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.TextField(default="/static/master/img/logo.png")
    tipo = models.ForeignKey(TipoMedio, related_name="tipo_medio", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="company_medio", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.nombre