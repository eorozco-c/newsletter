from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return redirect("usuarios:index")

@login_required(login_url='/')
def menu(request):
    return render(request, "menu.html")