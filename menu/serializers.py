from rest_framework import serializers
from .models import Fit, Food, Category, Set


class FitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fit
        fields = ["image", "title", "kcal", "price"]

class FoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "title image calories category".split()

class CategorySerializer(serializers.ModelSerializer):
    food = FoodListSerializer(many=True)    
    class Meta:
        model = Category
        fields = "category_name food".split()

class SetSerializer(serializers.ModelSerializer):
    foods = FoodListSerializer(many=True)
    class Meta:
        model = Set
        fields = "day foods fit".split()


class FitDetailSerializer(serializers.ModelSerializer):
    # set = SetSerializer(many=True)
    class Meta:
        model = Fit
        fields = "__all__"