from django.urls import  path
from . import views

app_name = "noticias"

urlpatterns = [
    path('',views.ObtenerData.as_view(), name="obtenernoticias" ),
]

