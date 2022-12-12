from rest_framework import serializers
from .models import Fit, Food, Category


class FitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fit
        fields = ["image", "title", "kcal", "price"]


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "title image calories carbohydrates squirrels fats ingredients".split()


class CategorySerializer(serializers.ModelSerializer):
    food = FoodListSerializer(many=True)
    class Meta:
        model = Category
        fields = "category_name food".split()


class FitDetailSerializer(serializers.ModelSerializer):
    food = FoodListSerializer(many=True)
    class Meta:
        model = Fit
        fields = "image title description kcal price food".split()
