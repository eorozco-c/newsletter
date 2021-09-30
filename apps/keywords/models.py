from django.db import models
from apps.companies.models import Company

# Create your models here.
class Keyword(models.Model):
    keywords = models.TextField()
    grupo = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company,related_name='keyword_company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)