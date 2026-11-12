from django.urls import path

from .views import index, contato, produto, prods, contats

urlpatterns = [
    path('index/', index),
    path('contato/', contato),
    path('contato/<int:pk>', contats, name="contato"),
    path('produto/<int:pk>', produto, name='produto'),
    path('produtos/', prods),
]