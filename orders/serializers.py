
from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import DishSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = OrderItem
        fields = ['dish', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'items']
