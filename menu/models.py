from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Submenu(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Dish(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField()
    submenu_id = models.ForeignKey(Submenu, on_delete=models.CASCADE)
