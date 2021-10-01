from django.urls import  path
from . import views

app_name = "estadisticas"

urlpatterns = [
    path('noticias-company', views.noticiasCompany, name="index"),
    path('populate-noticias-company', views.populateNoticiasCompany, name="populateNoticiasCompany"),
]
