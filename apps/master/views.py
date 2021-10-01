from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.noticias.models import Noticia
from apps.keywords.models import Keyword
# Create your views here.

def index(request):
    return redirect("usuarios:index")

@login_required(login_url='/')
def menu(request):
    context = {
        'keywords' : Keyword.objects.filter(company=request.user.company)
    } 
    return render(request, "menu.html", context)