from django.db import models

from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Submenu(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, related_name='submenus', on_delete=models.CASCADE)


class Dish(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField()
    submenu = models.ForeignKey(Submenu, related_name='dishes', on_delete=models.CASCADE)
