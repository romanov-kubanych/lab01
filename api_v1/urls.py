from django.urls import path, include
from rest_framework import routers

from api_v1 import views

app_name = 'api_v1'

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]