from django.urls import path, include
from rest_framework import routers

from menu.api_views import MenuAPIView, SubmenuViewSet, DishViewSet, MenuAPIViewCRUD, test_keyAPIView

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'menus/(?P<menu_id>\d+)/submenus', SubmenuViewSet, basename='menu-submenus')
# router.register(r'menus/(?P<menu_id>\d+)/submenus/(?P<submenu_id>\d+)/dishes', DishViewSet, basename='submenu-dishes')

urlpatterns = [
    path('test_key', test_keyAPIView.as_view()),
    path('menus', MenuAPIView.as_view()),
    path('menus/<int:menu_id>', MenuAPIViewCRUD.as_view())  # Добавляем путь с переменной menu_id
]
