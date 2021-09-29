from django.urls import  path
from . import views

app_name = "medios"

urlpatterns = [
    path('',views.NuevoMedio.as_view(), name="index" ),
    path('edit/<int:pk>',views.EditMedio.as_view(), name="medio_edit"),
    path('predestroy/<int:pk>',views.medio_predestroy, name="medio_predestroy"),
    path('destroy/<int:pk>',views.medio_destroy, name="medio_destroy"),
    path('tipo_medio',views.NuevoTipoMedio.as_view(), name="tipo_medio" ),
    path('tipo_medio/edit/<int:pk>',views.EditTipoMedio.as_view(), name="tipo_medio_edit"),
    path('tipo_medio/predestroy/<int:pk>',views.tipo_medio_predestroy, name="tipo_medio_predestroy"),
    path('tipo_medio/destroy/<int:pk>',views.tipo_medio_destroy, name="tipo_medio_destroy"),
]
