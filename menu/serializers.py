from rest_framework import serializers
from .models import Fit, Food


class FitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fit
        fields = ["title", "kcal", "price"]

class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class FitDetailSerializer(serializers.ModelSerializer):
    food = FoodListSerializer(many=True)
    class Meta:
        model = Fit
        fields = "title price kcal food".split()