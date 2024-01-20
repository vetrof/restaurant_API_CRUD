from rest_framework import serializers

from menu.models import Menu, Submenu, Dish


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('title', 'description')


class SubmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submenu
        fields = ('title', 'description', 'menu_id')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('title', 'description', 'submenu_id')
