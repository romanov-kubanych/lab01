from rest_framework import serializers

from webapp.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = []


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = []
