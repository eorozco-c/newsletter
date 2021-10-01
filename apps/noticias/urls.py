from django.urls import  path
from . import views

app_name = "noticias"

urlpatterns = [
    path('',views.ObtenerData.as_view(), name="obtenernoticias" ),
    path('predestroy/<int:pk>',views.noticia_predestroy, name="noticia_predestroy"),
    path('destroy/<int:pk>',views.noticia_destroy, name="noticia_destroy"),
]

