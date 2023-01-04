from rest_framework import serializers
from .models import Fit, Food, Category, WEEK_LIST


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category_name")


class FitListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Fit
        fields = ["image", "title", "kcal", "price", "category"]


class FoodListSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = "id day image category title calories carbohydrates squirrels fats ingredients".split()

    def get_day(self, instance):
        return WEEK_LIST[instance.day]

    def get_category(self, instance):
        return instance.category.category_name


class FitDetailSerializer(serializers.ModelSerializer):
    food = FoodListSerializer(many=True)

    class Meta:
        model = Fit
        fields = "__all__"
