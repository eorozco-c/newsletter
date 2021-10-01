from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .formularios import FormularioCompany
from .models import Company
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return HttpResponse("Companies")

@method_decorator(login_required, name='dispatch')
class ListCompany(ListView):
    model = Company
    template_name = "companies/companies.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser or Company.objects.count() == 0:
            return super().get(*args, **kwargs)
        return redirect("companies:index")

class CrearCompany(CreateView):
    template_name = "formularios/generico.html"
    form_class = FormularioCompany
    success_url = reverse_lazy("companies:index")

    def get_context_data(self, **kwargs):
        context = super(CrearCompany, self).get_context_data(**kwargs)
        context['title'] = "Nueva Comapañia"
        context['legend'] = "Registro Compañia"
        context['appname'] = "companies"
        return context

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser or Company.objects.count() == 0:
            return super().get(*args, **kwargs)
        return redirect("companies:index")

@method_decorator(login_required, name='dispatch')
class EditCompany(UpdateView):
    template_name = "companies/detalle_companies.html"
    model = Company
    form_class = FormularioCompany
    success_url = reverse_lazy("companies:index")

    def get_context_data(self, **kwargs):
        context = super(EditCompany, self).get_context_data(**kwargs)
        context['title'] = "Editar Company" 
        context['legend'] = "Editar Company"
        context['appname'] = "companies"
        return context
        
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser or Company.objects.count() == 0:
            return super().get(*args, **kwargs)
        return redirect("master:index")

@login_required(login_url="/")
def predestroy(request, pk):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=pk)
        except:
            return redirect("companies:index")
        context={
            'id' : company.id,
            'nombre': company.nombre,
        }
        return JsonResponse(context)
    return redirect("companies:index")

@login_required(login_url="/")
def destroy(request,pk):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=pk)
        except:
            return redirect("companies:index")
        try:
            company.delete()
        except:
            messages.success(request,f'No se puede eliminar Compañia ya que tiene elementos asignados',extra_tags='danger')
    return redirect("companies:index")