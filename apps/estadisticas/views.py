from apps.noticias.models import Noticia
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def noticiasCompany(request):
    return render(request,"estadisticas/noticias-company.html")

@login_required(login_url="/")
def populateNoticiasCompany(request):
    if request.method == "GET":
        labels = []
        data = []
        try:
            queryset = Noticia.objects.filter(company=request.user.company).values('keyword__grupo').annotate(noticias_company=Count('id'))
            for entry  in queryset:
                labels.append(entry['keyword__grupo'])
                data.append(entry['noticias_company'])
            context = {
                "labels" : labels,
                "data" : data,
            }
            return JsonResponse(context)
        except:
            return  JsonResponse({"response":"Error"})