from django.db import models

WEEK_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEK_CHOICES = ((day, day) for day in WEEK_LIST)
CATEGORY_LIST = ["breakfast", "lunch", "snack", "dinner"]
CATEGORY_CHOICES = ((category, category) for category in CATEGORY_LIST)



class Category(models.Model):
    category_name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.category_name

class Fit(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20)
    description = models.TextField()
    kcal = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.title

class Food(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, choices=CATEGORY_CHOICES)
    calories = models.PositiveSmallIntegerField()
    carbohydrates = models.PositiveSmallIntegerField()
    squirrels = models.FloatField()
    fats = models.FloatField()
    ingredients = models.TextField()

    def __str__(self) -> str:
        return self.title

FOOD_LIST = Food.objects.all()
FOOD_CHOICES = [(food.id, food.title) for food in FOOD_LIST]


class Set(models.Model):
    day = models.CharField(max_length=255, choices=WEEK_CHOICES)
    breakfast = models.CharField(max_length=255, choices=FOOD_CHOICES)
    lunch = models.CharField(max_length=255, choices=FOOD_CHOICES)
    snack = models.CharField(max_length=255, choices=FOOD_CHOICES)
    dinner = models.CharField(max_length=255, choices=FOOD_CHOICES)
    fit = models.ForeignKey(Fit, on_delete=models.PROTECT)