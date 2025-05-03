
from rest_framework import serializers
from .models import CartItem
from menu.serializers import DishSerializer

class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'dish', 'quantity']

class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['dish', 'quantity']
