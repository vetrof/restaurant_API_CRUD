from django.urls import path, include
from rest_framework import routers

from menu.api_views import MenuViewSet, SubmenuViewSet, DishViewSet


from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menus', MenuViewSet)
router.register(r'menus/(?P<menu_id>\d+)/submenus', SubmenuViewSet, basename='menu-submenus')
router.register(r'menus/(?P<menu_id>\d+)/submenus/(?P<submenu_id>\d+)/dishes', DishViewSet, basename='submenu-dishes')

urlpatterns = [
    path('', include(router.urls)),
]
