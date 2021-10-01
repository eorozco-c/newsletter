from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .formularios import FormularioTipoMedio, FormularioMedio
from django.contrib import messages
from .models import TipoMedio, Medio
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

@method_decorator(login_required, name='dispatch')
class NuevoMedio(ListView):
    model = Medio
    template_name = "medios/medios.html"

    def get_context_data(self, **kwargs):
        context = super(NuevoMedio, self).get_context_data(**kwargs)
        context['form'] = FormularioMedio()
        return context
    
    def post(self, request, *args, **kwargs):
        form = FormularioMedio(request.POST)
        if form.is_valid():
            medio = form.save(commit=False)
            medio.company = self.request.user.company
            medio.save()
            messages.success(request,'Agregado correctamente.', extra_tags='success')
        return redirect("medios:index")

    def get_queryset(self):
        queryset = Medio.objects.filter(company=self.request.user.company)
        return queryset

@method_decorator(login_required, name='dispatch')
class EditMedio(UpdateView):
    template_name = "formularios/generico.html"
    form_class = FormularioMedio
    model = Medio
    success_url = reverse_lazy("medios:index")

    def get_context_data(self, **kwargs):
        context = super(EditMedio, self).get_context_data(**kwargs)
        context['title'] = "Editar Medio" 
        context['legend'] = "Editar Medio"
        context['appname'] = "medios/"
        return context

@login_required(login_url="/")
def medio_predestroy(request, pk):
    if request.method == "GET":
        try:
            sector = Medio.objects.get(id=pk)
        except:
            return redirect("medios:index")
        context={
            'id' : sector.id,
            'nombre': sector.nombre,
        }
        return JsonResponse(context)
    return redirect("medios:index")

@login_required(login_url="/")
def medio_destroy(request,pk):
    if request.method == "GET":
        try:
            sector = Medio.objects.get(id=pk)
        except:
            return redirect("medios:index") 
        sector.delete()
        return redirect("medios:index") 
    messages.success(request,'Existen Trabajadores asociados al Sector que desea eliminar.', extra_tags='danger')
    return redirect("medios:index")  