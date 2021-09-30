from django.db import models
from apps.medios.models import Medio
from apps.companies.models import Company
from apps.keywords.models import Keyword

# Create your models here.

class Noticia(models.Model):
    contenido = models.TextField()
    url = models.CharField(max_length=255,unique=True)
    date = models.DateField()
    medio = models.ForeignKey(Medio, related_name="tipo_medio", on_delete=models.CASCADE)
    company = models.ForeignKey(Company,related_name="company_noticias", on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword,related_name="keyword_noticias", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.contenido