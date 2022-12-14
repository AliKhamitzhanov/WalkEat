from rest_framework import serializers
from .models import *

class MyOrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOrders
        fields = '__all__'
class CashBackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBack
        fields = '__all__'



