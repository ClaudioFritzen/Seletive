from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nova_vaga(request):
    return HttpResponse('Estou em nova vaga!')
