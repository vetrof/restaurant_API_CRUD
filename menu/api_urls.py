from django.urls import path, include
from rest_framework import routers

from menu.api_views import MenuViewSet

router = routers.DefaultRouter()
router.register(MenuViewSet)

urlpatterns = [
    path('', include(router.urls))
]
