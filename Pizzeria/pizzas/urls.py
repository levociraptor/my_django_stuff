from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('list_of_pizzas', views.pizzas, name='pizzas')
]
