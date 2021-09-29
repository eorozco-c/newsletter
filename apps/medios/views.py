from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .formularios import FormularioTipoMedio
from django.contrib import messages
from .models import TipoMedio
from django.http import JsonResponse
# Create your views here.
@method_decorator(login_required, name='dispatch')
class NuevoTipoMedio(ListView):
    model = TipoMedio
    template_name = "medios/tipos.html"

    def get_context_data(self, **kwargs):
        context = super(NuevoTipoMedio, self).get_context_data(**kwargs)
        context['form'] = FormularioTipoMedio()
        return context
    
    def post(self, request, *args, **kwargs):
        form = FormularioTipoMedio(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Agregado correctamente.', extra_tags='success')
        return redirect("medios:tipo_medio")

@method_decorator(login_required, name='dispatch')
class EditTipoMedio(UpdateView):
    template_name = "formularios/generico.html"
    form_class = FormularioTipoMedio
    model = TipoMedio
    success_url = reverse_lazy("medios:tipo_medio")

    def get_context_data(self, **kwargs):
        context = super(EditTipoMedio, self).get_context_data(**kwargs)
        context['title'] = "Editar Tipo Medio" 
        context['legend'] = "Editar Tipo Medio"
        context['appname'] = "medios/tipo_medio"
        return context

@login_required(login_url="/")
def tipo_medio_predestroy(request, pk):
    if request.method == "GET":
        try:
            sector = TipoMedio.objects.get(id=pk)
        except:
            return redirect("medios:tipo_medio")
        context={
            'id' : sector.id,
            'nombre': sector.nombre,
        }
        return JsonResponse(context)
    return redirect("medios:tipo_medio")

@login_required(login_url="/")
def tipo_medio_destroy(request,pk):
    if request.method == "GET":
        try:
            sector = TipoMedio.objects.get(id=pk)
        except:
            return redirect("medios:tipo_medio") 
        sector.delete()
        return redirect("medios:tipo_medio") 
    messages.success(request,'Existen Trabajadores asociados al Sector que desea eliminar.', extra_tags='danger')
    return redirect("medios:tipo_medio")  