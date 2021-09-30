from django.urls import  path
from . import views

app_name = "keywords"

urlpatterns = [
    path('',views.NuevoKeyword.as_view(), name="index" ),
    path('edit/<int:pk>',views.EditKeyword.as_view(), name="keyword_edit"),
    path('predestroy/<int:pk>',views.keyword_predestroy, name="keyword_predestroy"),
    path('destroy/<int:pk>',views.keyword_destroy, name="keyword_destroy"),
]
