from django.contrib import admin
from .models import Produto, Cliente, Contato


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Contato, ContatoAdmin)