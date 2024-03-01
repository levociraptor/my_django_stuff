from django.shortcuts import render
from .models import Meal


def index(request):
    """Главная страница, на котороой выводяться приемы пищи"""
    meals = Meal.objects.all().order_by('order')
    context = {'meals': meals}
    return render(request, 'meals/index.html', context)


def meal(request, meal_id):
    """Список блюд с их описанием для каждого приема пищи"""
    meal = Meal.objects.get(id=meal_id)
    dishes = meal.dish_set.all()
    context = {'meal': meal, 'dishes': dishes}
    return render(request, 'meals/meal.html', context)