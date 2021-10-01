from django.urls import  path
from . import views

app_name = "companies"

urlpatterns = [
    path('', views.ListCompany.as_view(), name="index"),
    path('crear', views.CrearCompany.as_view(), name="crear"),
    path('editar/<int:pk>', views.EditCompany.as_view(), name="editar"),
    path('predestroy/<int:pk>',views.predestroy, name="predestroy"),
    path('destroy/<int:pk>',views.destroy, name="destroy"),
]
