from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

from webapp.models import Product, Order
from api_v1.serializers import ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'head', 'option']

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAdminUser()]
        else:
            return [AllowAny()]
