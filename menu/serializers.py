from rest_framework import serializers

from menu.models import Menu, Submenu, Dish

from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    submenus_count = serializers.SerializerMethodField()
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'title', 'description', 'submenus_count', 'dishes_count')

    @staticmethod
    def get_submenus_count(obj):
        return obj.submenus.all().count()

    @staticmethod
    def get_dishes_count(obj):
        submenus = obj.submenus.all()
        dishes_count = Dish.objects.filter(submenu__in=submenus).count()
        return dishes_count


class SubmenuSerializer(serializers.ModelSerializer):
    dishes_count = serializers.SerializerMethodField()
    class Meta:
        model = Submenu
        fields = ('id', 'title', 'description', 'menu', 'dishes_count')

    @staticmethod
    def get_dishes_count(obj):
        return obj.dishes.all().count()


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'submenu')
