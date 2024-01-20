from django.db.models import Count
from rest_framework import serializers

from menu.models import Menu, Submenu, Dish

from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    submenus_count = serializers.IntegerField(read_only=True)
    dishes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'title', 'description', 'submenus_count', 'dishes_count')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['submenus_count'] = instance.submenus.count()
        representation['dishes_count'] = instance.submenus.annotate(
            dishes_count=Count('dishes')
        ).aggregate(total_dishes=Count('dishes_count'))['total_dishes']
        return representation


class SubmenuSerializer(serializers.ModelSerializer):
    dishes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submenu
        fields = ('id', 'title', 'description', 'dishes_count', 'menu')
        read_only_fields = ('menu',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['dishes_count'] = instance.dishes.count()
        return representation


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'submenu')
