from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from .formularios import FormularioRegistro, FormularioRegistroSU, FormularioEditar
from .models import Usuario
from apps.companies.models import Company
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):
    if request.method == "GET":
        if Company.objects.count() == 0:
            return redirect("companies:crear")
        if Usuario.objects.count() == 0:
            return redirect("usuarios:registrar")
        if request.user.is_authenticated:
            return redirect("master:menu")
    return redirect("login")


class Register(CreateView):
    template_name = "formularios/generico.html"
    success_url = reverse_lazy("master:index")

    def form_valid(self,form):
        usuario = form.save(commit = False)
        usuario.username = usuario.email
        usuario.set_password(usuario.password)
        usuario.save()
        login(self.request, usuario)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['title'] = "Registro" 
        context['legend'] = "Registro de usuario"
        return context

    def get_form_class(self):
        if self.request.user.is_superuser or Usuario.objects.count() == 0:
            return FormularioRegistroSU
        else:
            return FormularioRegistro

@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    template_name = "formularios/generico.html"
    model = Usuario
    form_class = FormularioEditar
    success_url = reverse_lazy("master:index")

    def get(self, request, pk):
        usuario = self.get_object()
        if self.request.user.company != usuario.company:
            return redirect("master:index")
        return super().get(request)