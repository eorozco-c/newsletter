from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .formularios import FormularioKeyword
from django.contrib import messages
from .models import Keyword
from django.http import JsonResponse

# Create your views here.
@method_decorator(login_required, name='dispatch')
class NuevoKeyword(ListView):
    model = Keyword
    template_name = "keywords/keywords.html"

    def get_context_data(self, **kwargs):
        context = super(NuevoKeyword, self).get_context_data(**kwargs)
        context['form'] = FormularioKeyword()
        return context
    
    def post(self, request, *args, **kwargs):
        form = FormularioKeyword(request.POST)
        if form.is_valid():
            keyword = form.save(commit=False)
            keyword.company = self.request.user.company
            keyword.save()
            messages.success(request,'Agregado correctamente.', extra_tags='success')
        return redirect("keywords:index")

@method_decorator(login_required, name='dispatch')
class EditKeyword(UpdateView):
    template_name = "formularios/generico.html"
    form_class = FormularioKeyword
    model = Keyword
    success_url = reverse_lazy("keywords:index")

    def get_context_data(self, **kwargs):
        context = super(EditKeyword, self).get_context_data(**kwargs)
        context['title'] = "Editar keywords" 
        context['legend'] = "Editar keywords"
        context['appname'] = "keywords/"
        return context

@login_required(login_url="/")
def keyword_predestroy(request, pk):
    if request.method == "GET":
        try:
            sector = Keyword.objects.get(id=pk)
        except:
            return redirect("keywords:index")
        context={
            'id' : sector.id,
            'nombre': sector.keywords,
        }
        return JsonResponse(context)
    return redirect("keywords:index")

@login_required(login_url="/")
def keyword_destroy(request,pk):
    if request.method == "GET":
        try:
            sector = Keyword.objects.get(id=pk)
        except:
            return redirect("keywords:index") 
        sector.delete()
        return redirect("keywords:index") 
    messages.success(request,'Existen Trabajadores asociados al Sector que desea eliminar.', extra_tags='danger')
    return redirect("keywords:index")  