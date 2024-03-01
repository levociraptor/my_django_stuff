from django.urls import path

from . import views

app_name = 'meals'
urlpatterns = [
    path('', views.index, name='index'),
    path('meal/<int:meal_id>/', views.meal, name='meal'),
]