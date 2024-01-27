from django.conf import settings
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from menu.models import Menu, Submenu, Dish
from menu.serializers import MenuSerializer, SubmenuSerializer, DishSerializer
from django.db.models import Count


class test_keyAPIView(APIView):
    def get(self, request):
        key = settings.TEST_KEY
        data = {'123': key}
        return Response(data)


class MenuAPIView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuAPIViewCRUD(APIView):
    def get(self, request, menu_id=None):
        if menu_id is not None:
            # Если указан id, возвращаем один объект или 404, если объект не найден
            menu = get_object_or_404(Menu, pk=menu_id)
            serializer = MenuSerializer(menu)
        else:
            # Если id не указан, возвращаем все объекты
            queryset = Menu.objects.all()
            serializer = MenuSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SubmenuViewSet(ModelViewSet):
    serializer_class = SubmenuSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']  # Получаем значение menu_id из аргументов представления
        return Submenu.objects.filter(menu=menu_id)

    def perform_create(self, serializer):
        # Получаем menu_id из аргументов представления
        menu_id = self.kwargs['menu_id']

        # Добавляем menu_id к данным перед сохранением
        serializer.save(menu_id=menu_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']
        submenu_id = self.kwargs['submenu_id']
        return Dish.objects.filter(submenu__menu=menu_id, submenu=submenu_id)
