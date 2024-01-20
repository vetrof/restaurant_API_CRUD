from rest_framework.viewsets import ModelViewSet

from menu.models import Menu, Submenu, Dish
from menu.serializers import MenuSerializer, SubmenuSerializer, DishSerializer
from django.db.models import Count


class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()



class SubmenuViewSet(ModelViewSet):
    serializer_class = SubmenuSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']  # Получаем значение menu_id из аргументов представления
        return Submenu.objects.filter(menu=menu_id)


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']
        submenu_id = self.kwargs['submenu_id']
        return Dish.objects.filter(submenu__menu=menu_id, submenu=submenu_id)
