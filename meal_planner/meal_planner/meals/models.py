from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Dish(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}\n{self.description[:50]}...'
