from apps.keywords.models import Keyword
from django.shortcuts import redirect
from .models import Noticia
from django.views.generic.list import ListView
from django.contrib import messages
from .formulario import FormularioData
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import twitter

# Create your views here.
@method_decorator(login_required, name='dispatch')
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
        keyword = request.POST['keyword']
        cantidad = request.POST['cantidad']
        if keyword == "" or cantidad == "":
            messages.success(request,'Campos obligatorios', extra_tags='danger')
            return redirect("noticias:obtenernoticias")
        tweets = twitter.obtenerTwitters(keyword, cantidad)
        company = self.request.user.company
        twitter.GrabarTwitters(tweets,company)
        messages.success(request,'Obtencion Realizada con exito.', extra_tags='success')
        return redirect("noticias:obtenernoticias")