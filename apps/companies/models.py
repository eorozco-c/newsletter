from django.db import models

# Create your models here.
class Company(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.TextField(default="/static/master/img/logo.png")
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.nombre