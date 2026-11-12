from django.shortcuts import render

from .models import Produto, Contato, Cliente


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
    prod = Produto.objects.get(id=pk)
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