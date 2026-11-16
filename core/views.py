from tempfile import template

from django.shortcuts import render
from .models import Produto, Contato, Cliente
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader



def index(request):
    context = {
        'Curso': 'Programação Web usando Django',
           }
    return render(request,'index.html', context)

def contato(request):
    conts = Contato.objects.all()
    context = {
        'conts': conts
    }
    return render(request,'contato.html', context)

def contats(request, pk):
    contatos = Contato.objects.get(id=pk)
    context = {
        'contats': contatos
    }
    return render(request,'conts.html', context)

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request,'produto.html', context)

def prods(request):
    prods = Produto.objects.all()
    context = {
        'produtos': prods
    }
    return render(request,'prods.html', context)

def error_404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf-8", status=404)

def error_500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf-8", status=500)
