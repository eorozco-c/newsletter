from django.shortcuts import render, redirect
from .models import Noticia
from django.views.generic.list import ListView
from django.contrib import messages
from .formulario import FormularioData
from . import twitter
from apps.keywords.models import Keyword

# Create your views here.

class ObtenerData(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"

    def get_context_data(self, **kwargs):
        context = super(ObtenerData, self).get_context_data(**kwargs)
        grupos = Keyword.objects.filter(company=self.request.user.company)
        context['grupos'] = grupos
        return context
    
    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        keyword =  Keyword.objects.get(id=request.POST['keyword'])
        cantidad = request.POST['cantidad']
        if keyword == "" or cantidad == "":
            messages.success(request,'Campos obligatorios', extra_tags='danger')
            return redirect("noticias:obtenernoticias")
        tweets = twitter.obtenerTwitters(keyword.keywords, cantidad)
        company = self.request.user.company
        twitter.GrabarTwitters(tweets,company,keyword)
        messages.success(request,'Obtencion Realizada con exito.', extra_tags='success')
        return redirect("noticias:obtenernoticias")
