from django.urls import  path
from . import views

app_name = "noticias"

urlpatterns = [
    path('obtenernoticias',views.ObtenerData.as_view(), name="obtenernoticias" ),
]

