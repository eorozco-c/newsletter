from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .formularios import FormularioCompany
from django.urls import reverse_lazy
from .models import Company
# Create your views here.

def index(request):
    return HttpResponse("Companies")

class CrearCompany(CreateView):
    template_name = "formularios/generico.html"
    form_class = FormularioCompany
    success_url = reverse_lazy("master:index")

    def get_context_data(self, **kwargs):
        context = super(CrearCompany, self).get_context_data(**kwargs)
        context['title'] = "Nueva Comapañia"
        context['legend'] = "Registro Compañia"
        context['appname'] = "companies"
        return context

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser or Company.objects.count() == 0:
            return super().get(*args, **kwargs)
        return redirect("master:index")