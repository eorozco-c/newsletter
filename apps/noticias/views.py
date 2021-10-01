from django.shortcuts import redirect
from .models import Noticia
from django.http import  JsonResponse
from django.views.generic.list import ListView
from django.contrib import messages
from . import twitter
from apps.keywords.models import Keyword
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

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
        if request.POST['keyword'] == "" or request.POST['cantidad'] == "":
            messages.success(request,'Ambos campos obligatorios', extra_tags='danger')
            return redirect("noticias:obtenernoticias")
        keyword =  Keyword.objects.get(id=request.POST['keyword'])
        cantidad = request.POST['cantidad']
        tweets = twitter.obtenerTwitters(keyword.keywords, cantidad)
        company = self.request.user.company
        twitter.GrabarTwitters(tweets,company,keyword)
        messages.success(request,'Obtencion Realizada con exito.', extra_tags='success')
        return redirect("noticias:obtenernoticias")

@login_required(login_url="/")
def noticia_predestroy(request, pk):
    if request.method == "GET":
        try:
            noticia = Noticia.objects.get(id=pk)
        except:
            return redirect("noticias:obtenernoticias")
        context={
            'id' : noticia.id,
            'nombre': noticia.contenido,
        }
        return JsonResponse(context)
    return redirect("noticias:obtenernoticias")

@login_required(login_url="/")
def noticia_destroy(request,pk):
    if request.method == "GET":
        try:
            noticia = Noticia.objects.get(id=pk)
        except:
            return redirect("noticias:obtenernoticias") 
        noticia.delete()
        return redirect("noticias:obtenernoticias") 
    messages.success(request,'Existen Trabajadores asociados a la noticia que desea eliminar.', extra_tags='danger')
    return redirect("noticias:obtenernoticias")  