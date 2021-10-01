from django.db import models
from apps.companies.models import Company

# Create your models here.
class Keyword(models.Model):
    keywords = models.TextField()
    grupo = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company,related_name='keyword_company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        for field_name in ['grupo']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Keyword, self).save(*args, **kwargs)