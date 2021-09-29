from django.urls import  path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.index, name="index"),
    path('registrar', views.Register.as_view(), name="registrar"),
    path('profile/<int:pk>', views.Profile.as_view(), name="profile"),
]
