from django.shortcuts import render
from .models import Pizza

def index(request):
    """Домашняя страница"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Страница где представленны все доступные виды пицц"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)