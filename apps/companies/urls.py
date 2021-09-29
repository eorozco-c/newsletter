from django.urls import  path
from . import views

app_name = "companies"

urlpatterns = [
    path('', views.index, name="index"),
    path('crear', views.CrearCompany.as_view(), name="crear"),
]
