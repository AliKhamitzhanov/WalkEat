from rest_framework import serializers
from cart.models import *


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class AdressesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresses
        fields = '__all__'


class CheckoutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'
