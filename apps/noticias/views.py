from django.shortcuts import render, redirect
from .models import Noticia
from django.views.generic.list import ListView
from django.contrib import messages
from .formulario import FormularioData
from . import twitter

# Create your views here.

class ObtenerData(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"

    def get_context_data(self, **kwargs):
        context = super(ObtenerData, self).get_context_data(**kwargs)
        context['form'] = FormularioData()
        return context
    
    def post(self, request, *args, **kwargs):
<<<<<<< Updated upstream
        form = FormularioData(request.POST)
        if form.is_valid():
            print("SSSSSSS")
            keyword = request.POST['keyword']
            company = self.request.user.company
            cantidad = request.POST['cantidad']
            tweets = twitter.obtenerTwitters(keyword, cantidad)
            twitter.GrabarTwitters(tweets,company)
            print("XXXXXXX")
            messages.success(request,'Obtencion Realizada con exito.', extra_tags='success')
        return redirect("medios:tipo_medio")
=======
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
>>>>>>> Stashed changes
