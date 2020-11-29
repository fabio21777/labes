from django.shortcuts import render

from .models import Carga

def acomp(request, usuario):
    filter = request.GET.get('filter')
    ordenador = request.GET.get('ordenador')

    if filter:
        cargas = Carga.objects.filter(status=filter, user=request.user) 
    elif ordenador:
        cargas = Carga.objects.all().order_by(ordenador).filter(user=request.user)
    else: 
        cargas = Carga.objects.all().order_by('-created_at').filter(user=request.user)

    return render(request,'core/acomp.html', {'usuario': usuario, 'cargas': cargas})

def addCarga(request):
    return render(request,'core/adicionar_carga.html')

def login(request):
    return render(request,'core/login.html')
