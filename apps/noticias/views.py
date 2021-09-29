from django.shortcuts import render, redirect
from .models import Noticia
from django.views.generic.list import ListView
from django.contrib import messages
from .formulario import FormularioData

# Create your views here.

class ObtenerData(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"

    def get_context_data(self, **kwargs):
        context = super(ObtenerData, self).get_context_data(**kwargs)
        context['form'] = FormularioData()
        return context
    
    def post(self, request, *args, **kwargs):
        form = FormularioData(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Obtencion Realizada con exito.', extra_tags='success')
        return redirect("medios:tipo_medio")